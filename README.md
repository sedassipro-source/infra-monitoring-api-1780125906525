# infra-monitoring-api-1780125906525

A FastAPI + PostgreSQL project: infra-monitoring-api-1780125906525

## Stack

- **Framework**: FastAPI
- **Database**: PostgreSQL (async via SQLAlchemy)
- **Deploy**: render



## Getting Started

```bash
cp .env.example .env
# Fill in DATABASE_URL and other variables

pip install -r requirements.txt
uvicorn src.main:app --reload
```

## API Endpoints

- `GET /health` — Health check

- `POST /webhooks` — Receive webhook events

## Environment Variables

See `.env.example` for required variables.
