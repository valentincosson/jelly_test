from typing import List
from pydantic import BaseModel

from ..models.character import GenderEnum, SpeciesEnum, StatusEnum


class Character(BaseModel):
    """This is the Character exposed by API"""

    id: int
    name: str
    status: StatusEnum
    species: SpeciesEnum
    type: str
    gender: GenderEnum

    class Config:
        orm_mode = True


class CharacterFull(BaseModel):
    from .episode import Episode

    id: int
    name: str
    status: StatusEnum
    species: SpeciesEnum
    type: str
    gender: GenderEnum
    episodes: List[Episode]

    class Config:
        orm_mode = True
