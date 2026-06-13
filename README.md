# Resources API

A FastAPI application that serves a CSV-backed list of resources with two endpoints:
- **List all resources** — returns every row from the CSV
- **Random pick per category** — returns one randomly selected resource from each category

---

## Project Structure

```
fastapi_app/
├── app/
│   ├── main.py                        # FastAPI instance & router registration
│   ├── dependencies.py                # Shared FastAPI dependencies (get_session)
│   ├── core/
│   │   └── config.py                  # pydantic-settings config (reads .env)
│   ├── api/v1/
│   │   ├── router.py                  # Aggregates all v1 routers
│   │   └── endpoints/
│   │       └── resources.py           # /resources/ and /resources/random
│   ├── crud/
│   │   └── resource.py                # Data access logic (CSV reads)
│   ├── db/
│   │   └── session.py                 # CSVSession (thin wrapper over csv.DictReader)
│   └── schemas/
│       └── resource.py                # Pydantic models: Resource, RandomPickResponse
├── data/
│   └── resources.csv                  # CSV "database" (title, type, category, notes, link)
├── tests/
│   ├── conftest.py                    # Fixtures: mock_session, TestClient
│   └── test_resources.py              # pytest test suite
├── Dockerfile                         # Multi-stage: development + production
├── docker-compose.yml                 # Development (hot reload, volume mount)
├── docker-compose.prod.yml            # Production (2 workers, non-root user)
├── requirements.txt
├── requirements-test.txt
└── pyproject.toml                     # pytest config
```

---

## Endpoints

| Method | Path                      | Description                          |
|--------|---------------------------|--------------------------------------|
| GET    | `/api/v1/resources/`      | List all resources                   |
| GET    | `/api/v1/resources/random`| One random pick per category         |
| GET    | `/health`                 | Health check                         |

Interactive docs available at `/docs` (Swagger) and `/redoc`.

---

## Getting Started

### 1. Environment

```bash
cp .env.example .env
```

### 2. Development (with Docker)

```bash
docker compose up --build
```

The app runs at `http://localhost:8000` with **hot reload** — edits to files under `app/` are reflected immediately without restarting the container.

### 3. Production

```bash
docker compose -f docker-compose.prod.yml up --build -d
```

Uses a non-root user and 2 Uvicorn workers.

---

## Running Tests

### Locally

```bash
pip install -r requirements-test.txt
pytest -v
```

### Inside Docker (dev container)

```bash
docker compose run --rm api pytest -v
```

---

## CSV Format

`data/resources.csv` uses the following columns:

| Column     | Required | Description                        |
|------------|----------|------------------------------------|
| `title`    | ✅       | Name of the resource               |
| `type`     | ✅       | e.g. `book`, `article`, `website`  |
| `category` | ✅       | e.g. `python`, `devops`            |
| `notes`    | ❌       | Short description                  |
| `link`     | ❌       | URL to the resource                |

To add new resources, simply edit `data/resources.csv` — no migrations needed.

---

## Configuration

All settings are in `.env` (see `.env.example`):

| Variable        | Default              | Description              |
|-----------------|----------------------|--------------------------|
| `APP_NAME`      | `Resources API`      | Title shown in /docs     |
| `APP_VERSION`   | `1.0.0`              | Version shown in /docs   |
| `DEBUG`         | `false`              | Enables debug mode       |
| `CSV_FILE_PATH` | `data/resources.csv` | Path to the CSV file     |
