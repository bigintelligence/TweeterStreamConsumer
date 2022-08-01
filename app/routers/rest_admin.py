from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.utils.database import get_db
from app.services.auth.secure_twitter_bearer import TwitterAuthBearer
from app.services.auth import admin_service

router = APIRouter(prefix='/auth/twitter/user', tags=["auth_twitter_user"],
                   responses={404: {"description": "Not found"}},
                   )

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.get('/oob')
async def rest_twitter_oob_url():
    return admin_service.get_twitter_oob_url()


@router.post('/pin')
async def rest_register_pin(pin: str, db: Session = Depends(get_db)):
    return admin_service.register_pin(pin, db)


@router.get('/check/token', dependencies=[Depends(TwitterAuthBearer())])
async def check_token_status():
    return {'token_status': 'ok'}

