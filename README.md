# API

A simple API blueprint

## Formatting

Use `poetry run black api`

## Testing

Use `poetry run pytest`


## Running the App in Development Mode
```
python -m uvicorn app.main:app --reload
```

Service's URL: http://127.0.0.1:8000/docs

## Alembic Migrations
Create:
```
alembic init alembic
alembic revision --autogenerate -m "Initial migration."
...
alembic revision --autogenerate -m "<My model change comment here...>"
```

Apply:

```
alembic upgrade head
```