from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.services.twitter.cruds import author_crud
from app.services.twitter.schemas.author_schema import AuthorCreate
from app.services.twitter.models.author_model import AuthorModel
from app.utils.logger import Logger

logger = Logger(__name__).logger


def create_author(author: AuthorCreate, db: Session):
    try:
        db_author: AuthorModel = author_crud.get_author(db, author.id)
        if db_author:
            logger.error(f'Author id {db_author.id} already exist')
            return db_author

        db_author: AuthorModel = author_crud.create_author(db, author)
        return db_author
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=500, detail=f'error creating author{author.dict()}.')


def get_authors_by_name(author_name: str, db: Session):
    try:
        return author_crud.get_authors_by_name(db, author_name)
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=500, detail=f'error reading authors by name{author_name}.')

