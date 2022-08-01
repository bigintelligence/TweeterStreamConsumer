from datetime import datetime
from pydantic import BaseModel
from app.services.twitter.schemas.author_schema import AuthorBase
from app.services.twitter.schemas.tweet_schema import Tweet


class AuthorReport(AuthorBase):
    creation_date: datetime
    tweets: list[Tweet]

    class Config:
        orm_mode = True


class Record(BaseModel):
    execution_datetime: datetime = datetime.now()
    records: int
    time_secs: float

    class Config:
        orm_mode = True


class Report(BaseModel):
    author_report: list[AuthorReport]
    records: list[Record]

    class Config:
        orm_mode = True

