from enum import Enum
import os


class ConfigProps(Enum):
    secret_consumer_key: str = os.environ.get('TWITTER_CONSUMER_KEY', '')
    secret_consumer_secret: str = os.environ.get('TWITTER_CONSUMER_SECRET', '')
    callback: str = 'oob'
    tweet_limit: int = 100
    timeout_secs: int = 30
    sleep_secs_to_check_status: int = 1

