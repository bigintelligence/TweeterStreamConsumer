import time
from datetime import datetime
from sqlalchemy.orm import Session
from app.services.twitter.models.pin_model import PinModel
from app.services.twitter.schemas.report_schema import Record
from app.utils.constants import ConfigProps
from app.services.twitter.operation.tweet_stream_handler import TweetStream
from app.services.twitter import record_service
from app.utils.logger import Logger

logger = Logger(__name__).logger


class TweetReport:
    def __init__(self, db: Session):
        self.db = db
        self._time_start_stream = time.perf_counter()
        self._tweet_limit = ConfigProps.tweet_limit.value
        self._timeout_secs = ConfigProps.timeout_secs.value
        self._sleep_secs_to_check_status = ConfigProps.sleep_secs_to_check_status.value
        self.execution_datetime = datetime.now()

    def search_tweets_by_keywords(self, filter_keywords: list, db_pin: PinModel):
        if db_pin:
            tweet_stream = TweetStream(self.db, self._tweet_limit, filter_keywords,
                                       ConfigProps.secret_consumer_key.value,
                                       ConfigProps.secret_consumer_secret.value,
                                       db_pin.token, db_pin.secret
                                       )
            # Filter realtime Tweets by keyword
            tweet_stream_thread = tweet_stream.filter(track=filter_keywords, threaded=True)
            while tweet_stream_thread.is_alive():
                time.sleep(self._sleep_secs_to_check_status)
                time_runing = round(time.perf_counter() - self._time_start_stream, 2)
                record = Record(execution_datetime=self.execution_datetime,
                                records=len(tweet_stream.tweet_list),
                                time_secs=time_runing)
                logger.info('tweets recordered: {} in {} secs '.format(record.records, record.time_secs))
                record_service.create_record(self.db, record)
                if time_runing > self._timeout_secs:
                    tweet_stream.disconnect()

