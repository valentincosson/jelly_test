from datetime import date
from typing import List

from pydantic import BaseModel


class Episode(BaseModel):
    id: int
    name: str
    air_date: date
    episode: int
    season: int

    class Config:
        orm_mode = True


class EpisodeFull(BaseModel):
    from .character import Character

    id: int
    name: str
    air_date: date
    episode: int
    season: int
    characters: List[Character]

    class Config:
        orm_mode = True
