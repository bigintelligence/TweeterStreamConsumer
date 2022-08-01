from unittest import mock

import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.utils.logger import Logger
from app.services.twitter.cruds import tweet_crud, author_crud

client = TestClient(app)
logger = Logger(__name__).logger


class TestRESTAuthorTweet:

    def mock_verify_token(self, db, token):
        logger.info(f'token_mock: {token}')
        return True

    def test_rest_author_create(self, object_author, token_header):
        with mock.patch('app.services.auth.secure_twitter_bearer.TwitterAuthBearer._verify_token',
                        self.mock_verify_token):
            client.headers = token_header
            response = client.post('/api/v1/authors/', json=object_author)
            logger.info("response: {} ".format(response.json()))
            assert response.status_code == 200
            assert response.json()['name'] == object_author['name']

    @pytest.mark.order(after='test_rest_author_create')
    def test_rest_author_by_name(self, object_author, token_header):
        with mock.patch('app.services.auth.secure_twitter_bearer.TwitterAuthBearer._verify_token',
                        self.mock_verify_token):
            client.headers = token_header
            response = client.get('/api/v1/authors/{}'.format(object_author['name']))
            assert response.status_code == 200
            assert len(response.json()) > 0
            assert response.json()[0]['name'] == object_author['name']

    @pytest.mark.order(after='test_rest_author_by_name')
    def test_rest_tweet_create(self, object_tweet, token_header):
        with mock.patch('app.services.auth.secure_twitter_bearer.TwitterAuthBearer._verify_token',
                        self.mock_verify_token):
            client.headers = token_header
            response = client.post('/api/v1/tweets/', json=object_tweet)
            logger.info("response: {} ".format(response.json()))
            assert response.status_code == 200
            assert response.json()['text'] == object_tweet['text']

    @pytest.mark.order(after='test_rest_tweet_create')
    def test_rest_tweet_by_author_id(self, object_tweet, token_header):
        with mock.patch('app.services.auth.secure_twitter_bearer.TwitterAuthBearer._verify_token',
                        self.mock_verify_token):
            client.headers = token_header
            response = client.get('/api/v1/tweets/{}'.format(object_tweet['author']['id']))
            assert response.status_code == 200
            assert len(response.json()) > 0

    @pytest.mark.order(after='test_rest_tweet_by_author_id')
    def test_del_tweet(self, db_session, object_tweet):
        tweet_deleted = tweet_crud.delete_tweet(db_session, object_tweet['id'])
        logger.info(f'tweet_deleted: {tweet_deleted}')
        assert tweet_deleted is not None

    @pytest.mark.order(after='test_del_tweet')
    def test_del_author(self, db_session, object_author):
        author_id_deleted = author_crud.delete_author(db_session, object_author['id'])
        assert author_id_deleted == object_author['id']

