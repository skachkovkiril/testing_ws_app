FROM node:latest

WORKDIR /app/

COPY js-websocket-app/package.json ./

RUN npm install

COPY js-websocket-app .

CMD ["node", "index.js"]