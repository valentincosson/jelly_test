from datetime import date
from typing import Optional

from pydantic import BaseModel


class CommentBase(BaseModel):
    episode_id: Optional[int]
    character_id: Optional[int]

    text: Optional[str]


class CommentUpdate(BaseModel):
    text: str


class CommentCreate(CommentBase):
    pass


class ParamsComment(CommentBase):
    pass


class Comment(CommentBase):
    id: int
    created_at = date
    updated_at = date

    class Config:
        orm_mode = True
