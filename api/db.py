import os

from sqlmodel import create_engine, Session


DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql://postgres:postgres@localhost/dev")

engine = create_engine(DATABASE_URL, echo=True)


def get_session():
    with Session(engine) as session:
        yield session