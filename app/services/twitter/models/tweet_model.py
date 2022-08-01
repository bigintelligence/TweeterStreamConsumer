from sqlalchemy.orm import relationship
from app.utils.database import Base
from sqlalchemy import Column, String, DateTime, ForeignKey, func


class TweetModel(Base):
    __tablename__ = 'tweets'

    id = Column(String, primary_key=True, index=True)
    creation_date = Column(DateTime, default=func.now())
    text = Column(String)
    author_id = Column(String, ForeignKey("authors.id"))
    author = relationship("AuthorModel", back_populates="tweets")

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

