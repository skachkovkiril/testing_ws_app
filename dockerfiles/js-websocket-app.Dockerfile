FROM node:12-alpine

WORKDIR /usr/src/app

COPY js-websocket-app/package*.json ./

RUN npm install

COPY js-websocket-app .