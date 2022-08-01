from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.services.auth.secure_twitter_bearer import TwitterAuthBearer
from app.utils.database import get_db
from app.services.twitter.schemas.author_schema import Author, AuthorCreate
from app.services.twitter import author_service

router = APIRouter(prefix='/authors', tags=["authors"],
                   responses={404: {"description": "Not found"}}
                   )


@router.post('/', dependencies=[Depends(TwitterAuthBearer())], response_model=Author)
async def rest_create_author(author: AuthorCreate, db: Session = Depends(get_db)):
    return author_service.create_author(author, db)


@router.get('/{author_name}', dependencies=[Depends(TwitterAuthBearer())], response_model=list[Author])
async def rest_get_authors_by_name(author_name: str, db: Session = Depends(get_db)):
    return author_service.get_authors_by_name(author_name, db)

