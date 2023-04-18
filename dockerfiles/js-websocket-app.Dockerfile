FROM node:latest

WORKDIR /app/

COPY js-websocket-app/package*.json ./

RUN npm install

COPY js-websocket-app .

EXPOSE 8000

CMD ["node", "index.js"]