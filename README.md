# Docker compose
## Work all applications
Run applications
```
make build

or

docker compose up --build -d --remove-orphans
```
Stop applications
```
make down

or

docker compose down
```

# WebSocket Applications
## FastAPI
To run a WebSocket application on FastAPI:
```
cd python-fastapi-app
pipenv shell
uvicorn main:app --reload
CTRL+C
exit
cd ..
```
## SANIC
To run a WebSocket application on Sanic:
```
cd python-sanic-app
pipenv shell
sanic main
CTRL+C
exit
cd ..
```
## Starlette
To run a WebSocket application on Starlette:
```
cd python-starlette-app
pipenv shell
uvicorn main:app --reload
CTRL+C
exit
cd ..
```
## Blacksheep
To run a WebSocket application on Blacksheep:
```
cd python-blacksheep-app
pipenv shell
uvicorn main:app --reload
CTRL+C
exit
cd ..
```
## Express.js (express-ws)
```
cd js-express-app
node index.js
CTRL+C
cd ..
```
## Tornado
To run a WebSocket application on Tornado:
```
cd python-tornado-app
pipenv shell
python server.py
CTRL+C
exit
cd ..
```
## Node.js WebSocket library (ws, http, url)
```
cd js-websocket-app
node index.js
CTRL+C
cd ..
```
## Asyncio/websockets
To run a WebSocket application on Asyncio:
```
cd python-asyncio-app
pipenv shell
python main.py
CTRL+C
exit
cd ..
```

# Testing application
To run a Testing application:
```
cd testing-app
pipenv shell
python main.py
> Enter the required number of clients
exit
cd ..
```