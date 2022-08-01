from sqlalchemy.orm import Session
from sqlalchemy import asc
from . import author_crud
from ..models.author_model import AuthorModel
from ..models.tweet_model import TweetModel
from ..schemas.tweet_schema import TweetCreate


def get_tweet(db: Session, tweet_id: str) -> TweetModel:
    return db.query(TweetModel)\
        .filter(TweetModel.id == tweet_id)\
        .first()


def get_tweets_by_author_id(db: Session, author_id: str) -> list[TweetModel]:
    return db.query(TweetModel)\
        .filter(TweetModel.author_id == author_id)\
        .order_by(asc(TweetModel.creation_date))\
        .all()


def create_tweet(db: Session, tweet: TweetCreate) -> TweetModel:
    db_author: AuthorModel = author_crud.get_author(db, tweet.author.id)
    db_author.tweets.append(TweetModel(id=tweet.id, text=tweet.text))
    return get_tweet(db, tweet.id)


def delete_tweet(db: Session, tweet_id: str) -> TweetModel:
    return db.query(TweetModel).filter(TweetModel.id == tweet_id).delete()

