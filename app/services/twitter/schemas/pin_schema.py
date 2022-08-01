from pydantic import BaseModel
from datetime import datetime


class PinBase(BaseModel):
    pin: str
    token: str
    secret: str


class PinCreate(PinBase):
    pass


class Pin(PinBase):
    creation_date: datetime

    class Config:
        orm_mode = True

