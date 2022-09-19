from pydantic import BaseModel


class JokeData(BaseModel):
    number: int
    phrase: str


class JokePhrase(BaseModel):
    phrase: str
