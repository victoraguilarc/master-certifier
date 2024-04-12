COMPOSE := @docker compose -f docker-compose.yml
COMPOSE_PROD := @docker compose -f docker-compose.prod.yml

install-serverless:
	npm install

install-python-requirements:
	pip install poetry
	poetry install

black:
	poetry run black fastapi_aws_starter_kit

flake8:
	poetry run flake8 fastapi_aws_starter_kit

deploy:
	npx sls deploy

serve:
	npx sls offline --noPrependStageInUrl


build:
	$(COMPOSE) build

up:
	@echo "Server up..."
	$(COMPOSE) up

shell:
	@echo "Opening container bash session"
	$(COMPOSE) run --rm fastapi bash

prod_build:
	$(COMPOSE_PROD) build

prod_up:
	@echo "Server up..."
	$(COMPOSE_PROD) up

prod_shell:
	@echo "Opening container bash session"
	$(COMPOSE_PROD) run --rm fastapi bash