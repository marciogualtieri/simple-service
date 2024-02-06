from fastapi import Depends, FastAPI, HTTPException

from . import crud
from .db import get_session

from . import models
from sqlmodel import Session


app = FastAPI()


@app.get("/users/", response_model=list[models.UserRead])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_session)):
    return crud.get_users(db, skip=skip, limit=limit)


@app.post("/users/", response_model=models.UserRead, status_code=201)
def create_user(user: models.UserCreate, session: Session = Depends(get_session)):
    db_user = crud.get_user_by_email(session, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(session=session, user=user)


@app.get("/users/{user_id}", response_model=models.UserRead)
def read_user(user_id: int, db: Session = Depends(get_session)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user