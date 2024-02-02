.DEFAULT_GOAL := help


.PHONY: help
help:
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.PHONY: up
up: ## run the project
	@make stop
	@docker compose up -d
	@make log

.PHONY: enable_local_env
enable_local_env: ## enable the local env
	@make local_env

.PHONY: ps
ps: ## ps command
	@docker compose ps

.PHONY: stop
stop: ## stop Docker containers without removing them
	@docker compose stop

.PHONY: rebuild
rebuild: ## rebuild base Docker images
	@docker compose down --remove-orphans
	@docker compose build --no-cache

.PHONY: reset
reset: ## update Docker images and reset local databases
	@docker compose down --volumes --remove-orphans
	@make up

.PHONY: pull
pull: ## update Docker images without losing local databases
	@docker compose down --remove-orphans
	@docker compose pull

.PHONY: bash
bash: ## open bash into project directory
	@docker exec -it focun-back-web-1 bash

.PHONY: test
test: ## start tests
	@export TESTING=on && make up

.PHONY: log
log: ## get only log of the django project
	@docker logs -f focun-back-web-1

.PHONY: logs
logs: ## get logs of all project
	@docker compose logs -f

.PHONY: fromscratch 
fromscratch: reset pull up