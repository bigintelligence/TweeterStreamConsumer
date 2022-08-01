from app.utils.database import Base
from sqlalchemy import Column, String, DateTime, func
from sqlalchemy.orm import relationship


class AuthorModel(Base):
    __tablename__ = 'authors'

    id = Column(String, primary_key=True, index=True)
    creation_date = Column(DateTime, default=func.now())
    name = Column(String)
    screen_name = Column(String)
    tweets = relationship("TweetModel", back_populates="author")

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
