from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from enum import Enum

from dataclasses import dataclass
from typing import Dict

from sendgrid.helpers.mail import Mail, To
from sendgrid import SendGridAPIClient

import os
import json
import aiohttp


app = FastAPI(title='emails-service')


@dataclass
class SendGridService:
    from_email: str = os.getenv('FROM_EMAIL')
    api_key: str = os.getenv('SENDGRID_API_KEY')

    async def load_template(self, message: object, template_id: str, dynamic_data: Dict[str, any]) -> None:
        message.template_id = template_id
        message.dynamic_template_data = dynamic_data

    async def send_email(self, to_email: str, template_id: str, dynamic_data: Dict[str, any]) -> int:
        try:
            message = Mail(self.from_email, To(to_email))
            await self.load_template(message, template_id, dynamic_data)
            sendgrid_client = SendGridAPIClient(self.api_key)
            response = sendgrid_client.send(message)
            return response.status_code
        except Exception as err:
            return err.status_code


@dataclass
class AuthService:
    oauth2_scheme: object = OAuth2PasswordBearer(tokenUrl='token')
    api_url: str = os.getenv('AUTH_API')

    async def authenticated(self, token: str = Depends(oauth2_scheme)) -> Dict[str, any]:
        headers = {'Authorization': f'Bearer {token}'}
        async with aiohttp.ClientSession(headers=headers) as session:
            try:
                async with session.post(f'{self.api_url}/authenticate') as response:
                    if response.status == 200:
                        return {'token': token}
                    else:
                        raise HTTPException(
                            status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Unauthorized',
                            headers={'WWW-Authenticate': 'Bearer'}
                        )
            except aiohttp.ClientConnectionError as err:
                return f'Error to authenticate token: {err}'


@dataclass
class OrderService:
    api_url: str = os.getenv('ORDERS_API')

    async def get_order(self, token: str, order_id: int) -> Dict[str, any]:
        headers = {'Authorization': f'Bearer {token}'}
        async with aiohttp.ClientSession(headers=headers) as session:
            try:
                async with session.get('{}/{}'.format(self.api_url, order_id)) as response:
                    if response.status == 200:
                        return json.loads(await response.text())
            except aiohttp.ClientConnectionError as err:
                return f'Error to get order {order_id}: {err}'

    async def map_order(self, order: Dict[str, any]) -> Dict[str, any]:
        order['totalPrice'] = '{:,}'.format(order['totalPrice'])
        order['items'] = list(map(lambda item: {
            'name': item['name'],
            'image': item['image'],
            'author': item['author'],
            'quantity': item['quantity'],
            'price': '{:,}'.format(item['price'])
        }, order['items']))
        return order


class EmailType(str, Enum):
    order = 'order'


class Email(BaseModel):
    item_id: int
    email_type: EmailType


@app.get('/email/status')
async def root() -> Dict[str, str]:
    return {'message': 'Emails service is running successfully'}


@app.post('/email/send')
async def send_email(email: Email, authenticated: bool = Depends(AuthService().authenticated)) -> Dict[str, str]:
    sendgrid_service = SendGridService()
    if email.email_type == EmailType.order:
        order_service = OrderService()
        order = await order_service.get_order(authenticated['token'], email.item_id)
        order_to_send = await order_service.map_order(order)
        if not order_to_send:
            raise HTTPException(status_code=404, detail='Order not found')
        status_code = await sendgrid_service.send_email(order_to_send['customer']['email'], os.getenv('ORDER_TEMPLATE_ID'), order_to_send)
        if status_code != 202:
            raise HTTPException(status_code=500, detail='Email not sent')
        else:
            return {'message': 'Email has been sent successfully'}
