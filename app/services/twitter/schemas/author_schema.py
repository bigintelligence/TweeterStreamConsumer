from pydantic import BaseModel
from datetime import datetime


class AuthorBase(BaseModel):
    id: str
    name: str
    screen_name: str


class AuthorCreate(AuthorBase):
    pass


class Author(AuthorBase):
    creation_date: datetime

    class Config:
        orm_mode = True

