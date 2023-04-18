FROM node:18-alpine

WORKDIR /app/

COPY js-express-app/package*.json /app/

RUN npm install

COPY js-express-app /app/

CMD ["node", "index.js"]