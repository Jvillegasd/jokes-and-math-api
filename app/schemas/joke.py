from pydantic import BaseModel


class JokeData(BaseModel):
    joker_id: int
    phrase: str


class JokerPhrase(BaseModel):
    phrase: str
