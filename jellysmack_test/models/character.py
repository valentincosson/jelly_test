import enum

from sqlalchemy import Column, Enum, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from ..db import Base
from .base import AssociativeModel, Model


class GenderEnum(str, enum.Enum):
    female = "Female"
    male = "Male"
    genderless = "Genderless"
    unknown = "Unknown"

    @classmethod
    def _missing_(cls, _):
        return GenderEnum.unknown


class StatusEnum(str, enum.Enum):
    dead = "Dead"
    alive = "Alive"
    unknown = "Unknown"

    @classmethod
    def _missing_(cls, _):
        return StatusEnum.unknown


class SpeciesEnum(str, enum.Enum):
    human = "Human"
    disease = "Disease"
    cronenberg = "Cronenberg"
    humanoid = "Humanoid"
    mythological_creature = "Mythological Creature"
    robot = "Robot"
    animal = "Animal"
    poopybutthole = "Poopybutthole"
    alien = "Alien"
    unknown = "Unknown"

    @classmethod
    def _missing_(cls, _):
        return SpeciesEnum.unknown


class CharacterEpisodesModel(Base, AssociativeModel):
    __tablename__ = "character_episodes"
    episode_id = Column(Integer, ForeignKey("episode.id"), primary_key=True)
    character_id = Column(Integer, ForeignKey("character.id"), primary_key=True)
    episode = relationship(
        "EpisodeModel",
        back_populates="characters",
    )
    character = relationship(
        "CharacterModel",
        back_populates="episodes",
    )


class CharacterModel(Base, Model):
    __tablename__ = "character"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String(255))
    status = Column(Enum(StatusEnum))
    species = Column(Enum(SpeciesEnum))
    type = Column(String(255))
    gender = Column(Enum(GenderEnum))

    episodes = relationship("CharacterEpisodesModel", back_populates="character")
    comments = relationship("CommentModel", back_populates="character")
