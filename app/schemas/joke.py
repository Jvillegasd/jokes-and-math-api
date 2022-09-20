from enum import Enum
from datetime import date

from pydantic import BaseModel


class JokeData(BaseModel):
    number: int
    phrase: str


class JokePhrase(BaseModel):
    phrase: str


class JokeDatabase(BaseModel):
    joke_id: int
    phrase: str
    created_at: date
    updated_at: date

    class Config:
        orm_mode = True


class JokeResources(str, Enum):
    dad = "Dad"
    chuck = "Chuck"
