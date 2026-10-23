IMAGE ?= simple-form-using-ajax-in-django
PORT ?= 8000
PYTHON ?= python3

.PHONY: setup migrate run superuser test docker-build docker-run clean

setup: ## Create virtualenv and install dependencies
	$(PYTHON) -m venv .venv && .venv/bin/pip install -r requirements-min.txt

migrate:
	.venv/bin/python manage.py migrate

run: migrate ## Run locally with mocks on http://localhost:$(PORT)
	USE_MOCKS=1 .venv/bin/python manage.py runserver $(PORT)

superuser:
	.venv/bin/python manage.py createsuperuser

test:
	.venv/bin/python manage.py test

docker-build:
	docker build -t $(IMAGE) .

docker-run: docker-build ## Run in Docker on http://localhost:$(PORT)
	docker run --rm -p $(PORT):8000 $(IMAGE)

clean:
	rm -rf .venv
	find . -name "__pycache__" -type d -prune -exec rm -rf {} +
