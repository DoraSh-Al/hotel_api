.PHONY: up down test lint

up:
    docker-compose up --build

down:
    docker-compose down

test:
    poetry run pytest

lint:
    poetry run ruff check .
