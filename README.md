# Genlogs Backend (FastAPI)

## Structure

- `main.py`: App entry point (FastAPI + CORS + router).
- `api/routes.py`: API endpoints (controllers).
- `api/services.py`: Business logic for carriers.
- `api/schemas.py`: Response models (contracts).

## Run

```
pip install -r requirements.txt
python -m uvicorn main:app --reload --port 3001
```

## Environment

```
ALLOWED_ORIGINS=http://localhost:5173,https://vercel-domain
```

## Endpoints

- `GET /health`
- `GET /carriers?from_city=...&to_city=...`

## Tests

```
pytest
```
