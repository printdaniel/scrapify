.PHONY: build run

build:
	docker-compose up -d --build

run:
	docker-compose run myapp
