from sqlalchemy.orm import Session
from sqlalchemy import and_
from ..schemas.pin_schema import PinCreate
from ..models.pin_model import PinModel


def get_pin_by_token_and_secret(db: Session, token: str, secret: str) -> PinModel:
    return db.query(PinModel)\
        .filter(and_(PinModel.token == token, PinModel.secret == secret))\
        .first()


def get_pin_by_token(db: Session, token: str) -> PinModel:
    return db.query(PinModel)\
        .filter(PinModel.token == token)\
        .first()


def create_access(db: Session, pin: PinCreate) -> PinModel:
    db_pin = PinModel(**pin.dict())
    db.add(db_pin)
    return db_pin

