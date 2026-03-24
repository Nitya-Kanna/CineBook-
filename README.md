# CineBook

Async Movie Seat Reservation system (FastAPI + PostgreSQL + Redis + Celery). Project covering relational modeling, race condition prevention, JWT auth, caching, and background jobs


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

## Project Progress

- Current phase: **Phase 3 (in progress)** — SQLAlchemy models and Alembic setup are added.
- Last completed milestone: **Phase 2** — schema design documented in [docs/schema.md](docs/schema.md).
- Next milestone: **Finish Phase 3** by generating and validating the initial Alembic migration from current models.

### Roadmap Status

- [x] Phase 1 — Project setup (`pyproject.toml`, env config, docker-compose, DB/session wiring)
- [x] Phase 2 — Data modeling and schema design
- [ ] Phase 3 — SQLAlchemy models and first migration
- [ ] Phase 4 — API layer (routes, schemas, dependencies)
- [ ] Phase 5 — Auth (JWT, bcrypt, register/login)
- [ ] Phase 6 — Race condition prevention (`SELECT FOR UPDATE`, transactions, Redis lock)
- [ ] Phase 7 — Redis caching (seat availability + invalidation)
- [ ] Phase 8 — Celery background jobs (email + booking expiry)
- [ ] Phase 9 — Testing (async tests + race-condition tests)
- [ ] Phase 10 — Deployment (Dockerfile, Nginx, Railway)
