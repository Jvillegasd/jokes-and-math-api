from pydantic import BaseModel


class AddedNumber(BaseModel):
    number: int


class LeastCommonMultiple(BaseModel):
    lcm: int
