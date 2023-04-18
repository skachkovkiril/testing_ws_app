FROM node:12-alpine

WORKDIR /usr/src/app

COPY js-express-app/package*.json ./

RUN npm install

COPY js-express-app .