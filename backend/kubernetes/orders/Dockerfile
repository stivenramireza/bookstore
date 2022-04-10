FROM node:14

WORKDIR /usr/src/app

COPY package*.json ./
RUN npm install

COPY . .

ENV PORT 3002
ENV DB_URI ${DB_URI}
ENV AUTH_API ${AUTH_API}
ENV EMAILS_API ${EMAILS_API}

CMD ["npm", "start"]
