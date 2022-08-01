from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.services.auth.auth_twitter_user import AuthTwitterUserHandler
from app.services.twitter.cruds import pin_crud
from app.services.twitter.schemas.pin_schema import PinCreate
from app.utils.logger import Logger

logger = Logger(__name__).logger


def get_twitter_oob_url():
    try:
        authorizer = AuthTwitterUserHandler()
        return {'url': authorizer.get_authorization_url()}
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=500, detail='error getting oob url.')


def register_pin(pin: str, db: Session):
    try:
        authorizer = AuthTwitterUserHandler()
        token, secret = authorizer.get_access_token_secret(pin)
        pin_object = PinCreate(pin=pin, token=token, secret=secret)
        pin_crud.create_access(db, pin_object)
        return {'token_type': 'bearer', 'token': token}
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=500, detail='error registering pin.')

