from sqlalchemy import Date, Column, Integer, String
from sqlalchemy.orm import relationship

from ..db import Base
from .base import Model


class EpisodeModel(Base, Model):
    __tablename__ = "episode"

    name = Column(String(255), unique=True, index=True)
    air_date = Column(Date)
    episode = Column(Integer)
    season = Column(Integer)

    characters = relationship("CharacterEpisodesModel", back_populates="episode")
