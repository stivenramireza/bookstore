FROM node:14

WORKDIR /usr/src/app

COPY package*.json ./
RUN npm install

COPY . .

ENV PORT 3001
ENV AWS_REGION ${AWS_REGION}
ENV AWS_COGNITO_USER_POOL_ID ${AWS_COGNITO_USER_POOL_ID}

CMD ["npm", "start"]
