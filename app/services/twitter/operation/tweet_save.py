from sqlalchemy.orm import Session
from app.services.twitter import tweet_service, author_service
from app.services.twitter.models.author_model import AuthorModel
from app.services.twitter.schemas.author_schema import AuthorCreate, Author
from app.services.twitter.schemas.tweet_schema import TweetCreate


def tweet_handler_save_db(db: Session, author: AuthorCreate, tweet: TweetCreate):
    db_author: AuthorModel = author_service.create_author(author, db)
    if db_author:
        tweet.author = Author(id=db_author.id,
                              name=db_author.name,
                              screen_name=db_author.screen_name,
                              creation_date=db_author.creation_date)
        tweet_service.create_tweet(tweet, db)

