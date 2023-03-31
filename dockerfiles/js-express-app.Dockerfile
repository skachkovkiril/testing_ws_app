FROM node:latest

WORKDIR /app/

COPY js-express-app/package*.json ./

RUN npm install

COPY js-express-app .

CMD ["node", "index.js"]