from typing import Optional
from pydantic import BaseModel

from ..models.character import GenderEnum, SpeciesEnum, StatusEnum


class BaseCharacter(BaseModel):
    name: Optional[str]
    status: Optional[StatusEnum]
    species: Optional[SpeciesEnum]
    type: Optional[str]
    gender: Optional[GenderEnum]

    class Config:
        orm_mode = True


class ParamsCharacter(BaseCharacter):
    pass


class Character(BaseCharacter):
    id: int
