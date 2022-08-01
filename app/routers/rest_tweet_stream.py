from fastapi import APIRouter, Request, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.auth.secure_twitter_bearer import TwitterAuthBearer
from app.services.twitter.cruds import pin_crud
from app.services.twitter.models.pin_model import PinModel
from app.services.twitter import tweet_report_service
from app.services.twitter.schemas.report_schema import Report
from app.utils.database import get_db
from app.utils.logger import Logger

router = APIRouter(prefix='/tweet_stream', tags=["tweet_stream"],
                   responses={404: {"description": "Not found"}}
                   )
logger = Logger(__name__).logger


def verify_token(req: Request, db: Session = Depends(get_db)) -> PinModel:
    token = req.headers["Authorization"][7:]
    db_pin = pin_crud.get_pin_by_token(db, token)
    if db_pin:
        logger.info(f'db_pin_founded: {db_pin.as_dict()["creation_date"]}')
        return db_pin
    raise HTTPException(status_code=500, detail='Could not get token.')


@router.post('/', dependencies=[Depends(TwitterAuthBearer())], response_model=Report)
async def rest_twitter_report(keywords: list[str], pin: PinModel = Depends(verify_token), db: Session = Depends(get_db)):
    return tweet_report_service.get_twitter_report(keywords, pin, db)

