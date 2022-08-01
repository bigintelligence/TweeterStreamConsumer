from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.services.auth.secure_twitter_bearer import TwitterAuthBearer
from app.utils.database import get_db
from app.services.twitter.schemas.tweet_schema import Tweet, TweetCreate
from app.services.twitter import tweet_service

router = APIRouter(prefix='/tweets', tags=["tweets"],
                   responses={404: {"description": "Not found"}}
                   )


@router.post('/', dependencies=[Depends(TwitterAuthBearer())], response_model=Tweet)
async def rest_create_tweet(tweet: TweetCreate, db: Session = Depends(get_db)):
    return tweet_service.create_tweet(tweet, db)


@router.get('/{author_id}', dependencies=[Depends(TwitterAuthBearer())], response_model=list[Tweet])
async def rest_get_tweets_by_author_id(author_id: str, db: Session = Depends(get_db)):
    return tweet_service.get_tweets_by_author_id(author_id, db)

