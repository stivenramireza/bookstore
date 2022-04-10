FROM python:3.8

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV PORT 8000
ENV SENDGRID_API_KEY ${SENDGRID_API_KEY}
ENV FROM_EMAIL ${FROM_EMAIL}
ENV AUTH_API ${AUTH_API}
ENV ORDERS_API ${ORDERS_API}
ENV ORDER_TEMPLATE_ID ${ORDER_TEMPLATE_ID}

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
