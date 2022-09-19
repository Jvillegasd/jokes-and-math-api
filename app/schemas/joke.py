from pydantic import BaseModel


class JokeData(BaseModel):
    joker_id: int
    phrase: str


class JokePhrase(BaseModel):
    phrase: str
