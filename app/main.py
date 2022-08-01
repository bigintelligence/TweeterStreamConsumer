from fastapi import FastAPI
from app.routers import rest_admin, rest_author, rest_tweet, rest_tweet_stream
from app.utils.logger import Logger
from app.utils.database import Base, engine

logger = Logger(__name__).logger
Base.metadata.create_all(bind=engine)
API_VERSION = '/api/v1'
ADMIN_VERSION = '/admin/v1'

app = FastAPI()
app.include_router(rest_admin.router, prefix=ADMIN_VERSION)
app.include_router(rest_author.router, prefix=API_VERSION)
app.include_router(rest_tweet.router, prefix=API_VERSION)
app.include_router(rest_tweet_stream.router, prefix=API_VERSION)


@app.get('/')
async def healthcheck():
    '''
    endpoint to healthcheck
    :return: JSON
    '''
    logger.info('init Healthckeck ok!!')
    return {'message': 'Healthckeck ok!!'}

