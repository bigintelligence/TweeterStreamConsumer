from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from app.services.twitter.schemas.author_schema import Author


class TweetBase(BaseModel):
    id: str
    text: str


class TweetCreate(TweetBase):
    author: Optional[Author]


class TweetWithAuthor(TweetBase):
    author: Optional[Author]
    creation_date: datetime

    class Config:
        orm_mode = True


class Tweet(TweetBase):
    creation_date: datetime

    class Config:
        orm_mode = True

