from sqlalchemy.orm import Session, selectinload
from sqlalchemy.sql import select
from ..schemas.author_schema import AuthorCreate
from ..models.author_model import AuthorModel


def get_author(db: Session, author_id: str) -> AuthorModel:
    return db.query(AuthorModel).filter(AuthorModel.id == author_id).first()


def get_authors_by_name(db: Session, author_name: str, skip: int = 0, limit: int = 100) -> list[AuthorModel]:
    return db.query(AuthorModel)\
        .filter(AuthorModel.name == author_name)\
        .offset(skip)\
        .limit(limit)\
        .all()


def get_tweets_grouped_by_author(db: Session) -> list[AuthorModel]:
    stmt = (select(AuthorModel).options(selectinload(AuthorModel.tweets)).order_by(AuthorModel.creation_date))
    return db.execute(stmt)


def create_author(db: Session, author: AuthorCreate) -> AuthorModel:
    db_author = AuthorModel(**author.dict())
    db.add(db_author)
    return get_author(db, db_author.id)


def delete_author(db: Session, author_id: str) -> str:
    db.query(AuthorModel).filter(AuthorModel.id == author_id).delete()
    return author_id

