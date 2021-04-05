
from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
from sqlalchemy.orm import Session


from .. import database, schemas, models
from ..hashing import Hash

from ..repository import user

routers = APIRouter(tags=['users'], prefix='/user')

get_db = database.get_db

@routers.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)


@routers.get('/', response_model=List[schemas.ShowUser])
def get_all_user(db: Session = Depends(get_db)):
    return user.get_all(db)

@routers.get('/{id}', response_model=schemas.ShowUser)
def get_one_user(id: int, db: Session = Depends(get_db)):
    return user.get_one(id, db)
