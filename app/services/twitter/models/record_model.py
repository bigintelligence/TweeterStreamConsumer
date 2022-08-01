from app.utils.database import Base
from sqlalchemy import Column, Integer, Float, DateTime, func


class RecordModel(Base):
    __tablename__ = 'records'
    id = Column(Integer, primary_key=True)
    execution_datetime = Column(DateTime, default=func.now())
    records = Column(Integer)
    time_secs = Column(Float)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
