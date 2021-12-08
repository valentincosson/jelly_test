from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from ..db import get_session
from ..models.episode import EpisodeModel
from ..schemas import Episode

router = APIRouter()


@router.get("/", response_model=List[Episode])
def read_episodes(db: Session = Depends(get_session)):
    return EpisodeModel.fetch_all(db)


@router.get("/{item_id}", response_model=Episode)
def read_episode(item_id, db: Session = Depends(get_session)):
    return EpisodeModel.fetch_by_id(db, item_id)
