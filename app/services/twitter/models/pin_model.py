from app.utils.database import Base
from sqlalchemy import Column, String, DateTime
import datetime


class PinModel(Base):
    __tablename__ = 'pin'

    pin = Column(String, primary_key=True)
    token = Column(String)
    secret = Column(String)
    creation_date = Column(DateTime, default=datetime.datetime.now())

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

