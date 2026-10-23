# Simple AJAX form + Channels (Django)

Django form submitted over AJAX, with a Channels consumer for live table updates.

> Status: minimal runnable version. Parts that were incomplete are marked with `TODO` in the code; external services are mocked.

## Quick start (Docker)

```sh
make docker-run        # builds the image and serves http://localhost:8000
```

## Quick start (local Python 3.7)

```sh
make setup             # creates .venv and installs requirements-min.txt
make run               # migrates SQLite and serves http://localhost:8000
make superuser         # optional: admin user for /admin
```

## Mocks

Controlled by `USE_MOCKS` (default `1`), added at the end of `task2/settings.py`:

- Channel layer is in-memory, so no Redis is needed.
- `requirements-min.txt` is a trimmed dependency list (the original `requirements.txt` includes MySQL/Postgres drivers that need system libraries).

## TODO

- `Procfile` runs `gunicorn task2.asgi`, which cannot serve WebSockets; use daphne for production.
- TODO: move `SECRET_KEY` out of source control before any deployment.
