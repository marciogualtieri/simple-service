import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlmodel import create_engine, Session, SQLModel

from api.main import app as main_app
from api.main import get_session

TEST_DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/test"

engine = create_engine(TEST_DATABASE_URL) 

def _get_test_session():
    db_session = Session(engine)
    try:
        yield db_session
    finally:
        db_session.close()


@pytest.fixture(scope="function")
def app():
   """
   Creates a fresh database for each test case.
   """
   SQLModel.metadata.create_all(engine)
   _app = main_app
   yield _app
   SQLModel.metadata.drop_all(engine)


@pytest.fixture(scope="function")
def db_connection(app: FastAPI):
   connection = engine.connect()
   connection.begin()


@pytest.fixture(scope="function")
def db_session(app: FastAPI, db_connection):
   """
   Creates a database session builder.
   """
   yield lambda: Session(engine)


@pytest.fixture(scope="function")
def client(app: FastAPI, db_connection):
   """
   Creates a new FastAPI TestClient.
   """
   app.dependency_overrides[get_session] = _get_test_session
   with TestClient(app) as client:
     yield client