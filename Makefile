DC = docker compose
ENV_PROD = .env.production
DC_DEV = $(DC) -f $(CURDIR)/.ci/docker-compose.yaml \
		--project-directory . \
		--env-file $(ENV_PROD) \
		--env-file user-service/$(ENV_PROD)

dev:
	test -f user-service/$(ENV_PROD) || cp user-service/.env.example user-service/$(ENV_PROD)
	$(DC_DEV) --profile dev up -d --build $(cont)

logs:
	$(DC_DEV) --profile dev logs $(cont) --tail 500

down:
	$(DC_DEV) --profile dev down
	
restart:
	$(DC_DEV) --profile dev restart $(cont)

.PHONY:tests