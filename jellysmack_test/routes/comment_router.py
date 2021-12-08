from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm.session import Session

from jellysmack_test.schemas.comment import CommentUpdate

from ..db import get_session
from ..models.comment import CommentModel
from ..schemas import Comment, CommentCreate

router = APIRouter(
    dependencies=[Depends(get_session)],
)


@router.get("/", response_model=List[Comment])
def read_comments(db: Session = Depends(get_session)):
    return CommentModel.fetch_all(db)


@router.get("/{item_id}", response_model=Comment)
def read_comment(item_id: int, db: Session = Depends(get_session)):
    return CommentModel.fetch_by_id(db, item_id)


@router.post("/", response_model=Comment, status_code=201)
def create_comment(comment: CommentCreate, db: Session = Depends(get_session)):
    if not comment.character_id and not comment.episode.id:
        raise HTTPException(
            status_code=400,
            detail="Please specify at least episode_id or character id.",
        )
    return CommentModel.create(db, comment)


@router.patch("/{item_id}", response_model=Comment)
def update_comment(
    item_id: int, comment: CommentUpdate, db: Session = Depends(get_session)
):
    updated_comment = CommentModel.update(db, item_id, comment)
    if not updated_comment:
        raise HTTPException(
            status_code=404,
            detail="This comment doesn't exist.",
        )
    return updated_comment


@router.delete("/{item_id}", status_code=204)
def delete_comment(item_id: int, db: Session = Depends(get_session)):
    if not CommentModel.delete(db, item_id):
        raise HTTPException(
            status_code=404,
            detail="This comment doesn't exist.",
        )
