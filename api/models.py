from sqlmodel import SQLModel, Field, Relationship


class UserBase(SQLModel):
    email: str


class User(UserBase, table=True):
    id: int = Field(default=None, nullable=False, primary_key=True)
    hashed_password: str


class UserCreate(UserBase):
    password: str


class UserRead(UserBase):
    id: int
