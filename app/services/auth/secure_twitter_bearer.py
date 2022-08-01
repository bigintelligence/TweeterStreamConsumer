from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Request, HTTPException, Depends
from sqlalchemy.orm import Session
from app.services.twitter.cruds import pin_crud
from app.utils.database import get_db
from app.utils.logger import Logger

logger = Logger(__name__).logger


class TwitterAuthBearer(HTTPBearer):
    def __init__(self):
        super(TwitterAuthBearer, self).__init__()

    async def __call__(self, request: Request, db: Session = Depends(get_db)):
        credentials: HTTPAuthorizationCredentials = await super(TwitterAuthBearer, self).__call__(request)
        logger.info(f'cretentials: {credentials}')
        if credentials:
            if not credentials.scheme == 'Bearer':
                raise HTTPException(status_code=403, detail='Invalid authentication scheme.')
            if not self._verify_token(db, credentials.credentials):
                raise HTTPException(status_code=403, detail='Invalid token or expired token.')
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail='Invalid authorization code.')

    @staticmethod
    def _verify_token(db: Session, token: str) -> bool:
        logger.info(f'token: {token}')
        db_pin = pin_crud.get_pin_by_token(db, token)
        if db_pin:
            logger.info(f'db_pin_created: {db_pin.as_dict()["creation_date"]}')
            return True
        return False

