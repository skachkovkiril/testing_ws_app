DC = docker-compose
START = up --build -d --remove-orphans

build:
	$(DC) $(START)

down:
	$(DC) down

show:
	$(DC) logs
