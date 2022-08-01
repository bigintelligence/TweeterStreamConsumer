from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.services.twitter.cruds import tweet_crud
from app.services.twitter.schemas.tweet_schema import TweetCreate
from app.services.twitter.models.tweet_model import TweetModel
from app.utils.logger import Logger

logger = Logger(__name__).logger


def create_tweet(tweet: TweetCreate, db: Session):
    try:
        if tweet_crud.get_tweet(db, tweet.id):
            logger.error(f'Tweet id {tweet.id} already exist')
            raise HTTPException(status_code=400, detail='Author id already exist')

        db_tweet: TweetModel = tweet_crud.create_tweet(db, tweet)
        return db_tweet
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=500, detail=f'error creating tweet. {tweet.dict()}')


def get_tweets_by_author_id(author_id: str, db: Session):
    try:
        return tweet_crud.get_tweets_by_author_id(db, author_id)
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=500, detail=f'error reading tweets from author_id. {author_id}')
