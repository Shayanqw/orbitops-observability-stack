.PHONY: up down smoke lint test compose-validate

up:
	docker compose up --build

down:
	docker compose down -v

smoke:
	./scripts/smoke_test.sh

lint:
	ruff check demo_api

test:
	pytest -q demo_api/tests

compose-validate:
	docker compose config -q
