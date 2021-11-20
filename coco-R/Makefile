all:
	@echo "Hello $(LOGNAME), nothing to do by default"
	@echo "Try 'make help'"

help: ## This help.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

validate_env:
	@command -v docker > /dev/null || (echo "You need to install docker and docker-compose before proceeding" && exit 1)
	@command -v docker-compose > /dev/null || (echo "You need to install docker and docker-compose before proceeding" && exit 1)

build: delete-container ## Build the container
	@docker-compose build
	@docker-compose up -d

restart: ## Restart the container
	@docker-compose restart

cmd: start ## Access bash
	@docker-compose exec java /bin/bash

start:
	@docker-compose start

down: ## Stop container
	@docker-compose stop || true

delete-container: down
	@docker-compose down || true

remove: delete-container ## Delete containers and images

.DEFAULT_GOAL := help
