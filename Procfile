service: uvicorn api.main:app --host 0.0.0.0 --port 8888
test: pytest -s -vv
runserver: uvicorn api.main:app --reload
migrate: alembic upgrade head