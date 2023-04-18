FROM node:18-alpine

WORKDIR /app/

COPY js-websocket-app/package*.json /app/

RUN npm install

COPY js-websocket-app /app/

CMD ["node", "index.js"]