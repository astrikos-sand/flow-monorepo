build:
	docker compose up --build -d

up:
	docker compose up -d

down:
	docker compose down

prod-up:
	docker compose -f astrikos/setup.docker-compose.yml up --build -d 
	docker compose -f astrikos-worker/setup.docker-compose.yml up --build -d

prod-down:
	docker compose -f astrikos/setup.docker-compose.yml down
	docker compose -f astrikos-worker/setup.docker-compose.yml down