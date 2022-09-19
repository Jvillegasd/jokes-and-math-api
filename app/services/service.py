import math
from typing import List

from app.models.joke import Joke
from app.schemas.joke import JokeData
from app.errors.service import (
  EmptyList,
  JokeUpdateError
)
from app.services.interfaces.service_in import IService
from app.repository.interfaces.repository_in import IRepository

from sqlalchemy.exc import DatabaseError


class Service(IService):

    def __init__(self, repository: IRepository):
        super().__init__(repository)

    async def get_random_joke(self) -> str:
        return await self.respository.get_random_joke()

    async def get_joke_from_resource(self, resource: str) -> str:
        return await self.respository.get_joke_from_resource(resource)

    async def create_joke(self, phrase: str) -> JokeData:
        return await self.respository.create_joke(phrase)

    async def update_joke(self, joke_id: int, new_phrase: str) -> JokeData:
        try:
            updated_joke = await self.respository.update_joke(
                joke_id,
                new_phrase
            )
        except (Exception, DatabaseError):
            raise JokeUpdateError('Could not update provided joke')
        return updated_joke

    async def delete_joke(self, joke_id: int):
        await self.respository.delete_joke(joke_id)

    async def get_jokes(self) -> List[Joke]:
        return await self.respository.get_jokes()

    async def least_common_multiple(
        self,
        numbers: List[int]
    ) -> int:
        if not numbers:
            raise EmptyList('LCM array is empty, cannot make calculation')

        lcm = numbers[0]
        for i in range(1, len(numbers)):
            lcm = lcm * numbers[i] // math.gcd(lcm, numbers[i])
        return lcm

    async def add_one_to_number(self, number: int) -> int:
        return number + 1
