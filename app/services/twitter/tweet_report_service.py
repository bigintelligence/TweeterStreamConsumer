from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.services.twitter.models.pin_model import PinModel
from app.services.twitter.operation.tweet_report import TweetReport
from app.services.twitter.cruds import record_crud, author_crud
from app.services.twitter.schemas.report_schema import AuthorReport, Report
from app.services.twitter.schemas.tweet_schema import Tweet
from app.utils.logger import Logger

logger = Logger(__name__).logger


def get_twitter_report(keywords: list[str], pin: PinModel, db: Session):
    try:
        tweets_report = []
        report = TweetReport(db)
        # execute the streamer
        report.search_tweets_by_keywords(keywords, pin)
        tweets_db_result = author_crud.get_tweets_grouped_by_author(db)
        tweets_db_records = record_crud.get_records(db)
        for row in tweets_db_result:
            author_tweets = [Tweet(id=tweet.id, text=tweet.text, creation_date=tweet.creation_date) for tweet in row[0].tweets]
            author_report = AuthorReport(id=row[0].id,
                                         name=row[0].name,
                                         screen_name=row[0].screen_name,
                                         creation_date=row[0].creation_date,
                                         tweets=author_tweets)
            tweets_report.append(author_report)
        if len(tweets_report) > 0:
            return Report(author_report=tweets_report, records=tweets_db_records)
        raise HTTPException(status_code=400, detail='report empty')
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=500, detail='error generating report.')


