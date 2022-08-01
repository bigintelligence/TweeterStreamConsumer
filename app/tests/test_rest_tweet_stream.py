from unittest import mock
from fastapi.testclient import TestClient
from app.main import app
from app.routers.rest_tweet_stream import verify_token
from app.services.twitter.models.pin_model import PinModel
from app.utils.logger import Logger

logger = Logger(__name__).logger


async def override_dependency_verify_token():
    logger.info('pin_mocked')
    return PinModel()

app.dependency_overrides[verify_token] = override_dependency_verify_token
client = TestClient(app)


class TestRESTTweetStream:
    def mock_search_tweets(self, keywords, pin):
        logger.info(f'searching_mock: {keywords}')
        pass

    def mock_verify_token(self, db, token):
        logger.info(f'token_mock: {token}')
        return True

    def test_rest_get_report(self, keywords_list, token_header):
        with mock.patch('app.services.auth.secure_twitter_bearer.TwitterAuthBearer._verify_token',
                        self.mock_verify_token):
            with mock.patch('app.services.twitter.operation.tweet_report.TweetReport.search_tweets_by_keywords',
                            self.mock_search_tweets):
                client.headers = token_header
                response = client.post('/api/v1/tweet_stream/', json=keywords_list)
                logger.info("response: {} ".format(response.json()))
                assert response.status_code == 200
                assert type(response.json()['author_report']) == list
                assert type(response.json()['records']) == list

