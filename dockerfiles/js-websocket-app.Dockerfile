FROM node:18-alpine

WORKDIR /app/

COPY js-websocket-app/package*.json ./

RUN npm install

COPY js-websocket-app .

CMD ["node", "app/index.js"]