from sqlmodel import Session, select
from . import models


def get_user(session: Session, user_id: int):
    return session.exec(select(models.User).where(models.User.id == user_id)).first()


def get_user_by_email(session: Session, email: str):
    return session.exec(select(models.User).where(models.User.email == email)).first()


def get_users(session: Session, skip: int = 0, limit: int = 100):
    return session.exec(select(models.User).offset(skip).limit(limit)).all()


def create_user(session: Session, user: models.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    user = models.User(email=user.email, hashed_password=fake_hashed_password)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

