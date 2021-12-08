from sqlalchemy import ForeignKey, Column, String, Date
from sqlalchemy.orm import relationship
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.functions import func

from ..db import Base
from ..schemas.comment import CommentCreate, CommentUpdate

from .base import Model


class CommentModel(Base, Model):
    __tablename__ = "comment"

    created_at = Column(Date, nullable=False, default=func.now())
    updated_at = Column(Date, nullable=False, default=func.now(), onupdate=func.now())

    episode_id = Column(ForeignKey("episode.id"), nullable=True)
    character_id = Column(ForeignKey("character.id"), nullable=True)
    episode = relationship("EpisodeModel", back_populates="comments")
    character = relationship("CharacterModel", back_populates="comments")

    text = Column(String)

    @classmethod
    def create(cls, session: Session, obj: CommentCreate):
        instance = CommentModel(
            episode_id=obj.episode_id, character_id=obj.character_id, text=obj.text
        )
        return cls._create(session, instance)

    @classmethod
    def update(cls, session: Session, obj_id: int, obj: CommentUpdate):
        update = {CommentModel.text: obj.text}
        return cls._update(session, obj_id, update)
