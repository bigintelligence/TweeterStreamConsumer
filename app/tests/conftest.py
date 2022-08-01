import pytest
from datetime import datetime
from app.utils.database import SessionLocal


@pytest.fixture(scope='session')
def db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture(scope='session')
def object_author():
    return {
            "id": "123",
            "creation_date": datetime.now().strftime('%Y-%m-%dT%H:%M:%S'),
            "name": "test",
            "screen_name": "test"
        }


@pytest.fixture(scope='session')
def object_tweet(object_author):
    return {
            "id": "123",
            "creation_date": datetime.now().strftime('%Y-%m-%dT%H:%M:%S'),
            "text": "test",
            "author": object_author
        }


@pytest.fixture(scope='session')
def keywords_list():
    return ['bieber']


@pytest.fixture(scope='session')
def token_header():
    return {'Authorization': 'Bearer token'}

