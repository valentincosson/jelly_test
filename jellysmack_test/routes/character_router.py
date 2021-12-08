from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from ..db import get_session

from ..models.character import CharacterModel
from ..schemas import Character

router = APIRouter()


@router.get("/", response_model=List[Character])
def read_characters(db: Session = Depends(get_session)):
    return CharacterModel.fetch_all(db)


@router.get("/{item_id}", response_model=Character)
def read_character(item_id, db: Session = Depends(get_session)):
    return CharacterModel.fetch_by_id(db, item_id)
