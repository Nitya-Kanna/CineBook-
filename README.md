# CineBook

Async Movie Seat Reservation system (FastAPI + PostgreSQL + Redis + Celery). Project covering relational modeling, race condition prevention, JWT auth, caching, and background jobs

**Phase 2 — data model:** see [docs/schema.md](docs/schema.md) (tables, enums, constraints, indexes).

## Prerequisites

- Python **3.11+** (use `python3.11 -m venv .venv` if your default `python3` is newer and wheels fail to install)
- Docker / Colima / Docker Desktop running (for `docker-compose` / `docker compose` against the daemon)

## Setup

1. Copy environment template and edit if needed:

   ```bash
   cp .env.example .env
   ```

2. Start infrastructure (use `docker-compose` if the Compose v2 plugin is not installed):

   ```bash
   docker compose up -d
   ```

   Wait until Postgres is healthy (`docker compose ps` or `docker-compose ps`). `/health/db` requires Postgres to be up and reachable at `DATABASE_URL`.

3. Create a virtual environment and install the app with dev tools:

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Windows: .venv\Scripts\activate
   pip install -e ".[dev]"
   ```

4. Run the API:

   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

5. Check endpoints:

   - [http://127.0.0.1:8000/health](http://127.0.0.1:8000/health) — process up
   - [http://127.0.0.1:8000/health/db](http://127.0.0.1:8000/health/db) — database reachable

## Environment variables

See [.env.example](.env.example). `DATABASE_URL` must use the `postgresql+asyncpg://` scheme for the async engine.

## Tooling

- Lint: `ruff check app`
- Tests (later phases): `pytest`
