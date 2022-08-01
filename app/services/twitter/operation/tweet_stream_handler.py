import json
import tweepy
from sqlalchemy.orm import Session

from app.services.twitter.schemas.author_schema import AuthorCreate
from app.services.twitter.schemas.tweet_schema import TweetCreate
from app.services.twitter.operation import tweet_save
from app.utils.logger import Logger

logger = Logger(__name__).logger


class TweetStream(tweepy.Stream):

    def __init__(self, db: Session, limit: int, keywords: list,
                 consumer_key: str, consumer_secret: str,
                 access_key: str, access_secret: str):
        self.db = db
        self.tweet_key_text = 'text'
        self.key_id = 'id'
        self.user_key = 'user'
        self.user_key_name = 'name'
        self.user_key_screen_name = 'screen_name'
        self.tweet_list = []
        self.limit = limit
        self.keywords = keywords
        super().__init__(consumer_key, consumer_secret, access_key, access_secret)

    def on_closed(self, response):
        try:
            logger.info(response)
            logger.info(len(self.tweet_list))
            # if it has to be the exact limit
            if len(self.tweet_list) > self.limit:
                self.tweet_list = self.tweet_list[:self.limit]
        except Exception as e:
            logger.error(e)

    def on_data(self, raw_data):
        try:
            if len(self.tweet_list) <= self.limit:
                data = json.loads(raw_data)
                user_author: AuthorCreate = AuthorCreate(id=data[self.user_key][self.key_id],
                                                         name=data[self.user_key][self.user_key_name],
                                                         screen_name=data[self.user_key][self.user_key_screen_name])
                tweet: TweetCreate = TweetCreate(id=data[self.key_id],
                                                 text=data[self.tweet_key_text])
                tweet_save.tweet_handler_save_db(self.db, user_author, tweet)
                self.tweet_list.append((user_author, tweet))
                logger.info(user_author.dict())
                logger.info(tweet.dict())
            else:
                self.disconnect()
        except Exception as e:
            self.disconnect()
            logger.error(e)

