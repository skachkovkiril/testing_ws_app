FROM node:18-alpine

WORKDIR /app/

COPY js-express-app/package*.json ./

RUN npm install

COPY js-express-app .

CMD ["node", "app/index.js"]