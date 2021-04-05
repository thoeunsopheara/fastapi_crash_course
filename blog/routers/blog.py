
from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
from sqlalchemy.orm import Session

from .. import schemas, database, models
from ..repository import blog
from ..oauth2 import get_current_user


routers = APIRouter(tags=['blogs'], prefix='/blog')
get_db = database.get_db

@routers.post('/', response_model=schemas.ShowBlog, status_code=status.HTTP_201_CREATED)
def add_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.create(request, db)

@routers.delete('/{id}', status_code=status.HTTP_202_ACCEPTED)
def delete_blog(id, db: Session = Depends(get_db)):
    return blog.delete(id, db)

@routers.put('/{id}', response_model=schemas.ShowBlog, status_code=status.HTTP_202_ACCEPTED)
def update_blog(id, request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.update(id, db)

@routers.get('/',response_model=List[schemas.ShowBlog])
def get_all_blogs(db: Session = Depends(get_db), get_current_user: schemas.User=Depends(get_current_user)):
    return blog.get_all(db)

@routers.get('/{id}', response_model=schemas.ShowBlog)
def get_one_blog(id, db: Session = Depends(get_db), status_code=status.HTTP_200_OK):
    return blog.get_one(id, db)
