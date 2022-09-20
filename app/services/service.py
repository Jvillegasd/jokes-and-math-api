import math
from typing import List

from app.models.joke import Joke
from app.schemas.joke import (
    JokeData,
    JokePhrase
)
from app.errors.service import (
    EmptyList,
    JokeUpdateError,
    InsufficientListSize
)
from app.services.interfaces.service_in import IService
from app.repository.interfaces.repository_in import IRepository
from app.schemas.number import (
    AddedNumber,
    LeastCommonMultiple
)

from sqlalchemy.exc import DatabaseError


class Service(IService):

    def __init__(self, repository: IRepository):
        super().__init__(repository)

    async def get_random_joke(self) -> JokePhrase:
        random_joke = await self.repository.get_random_joke()
        return JokePhrase(phrase=random_joke)

    async def get_joke_from_resource(self, resource: str) -> JokePhrase:
        random_joke = await self.repository.get_joke_from_resource(resource)
        return JokePhrase(phrase=random_joke)

    async def create_joke(self, phrase: str) -> JokeData:
        return await self.repository.create_joke(phrase)

    async def update_joke(self, joke_id: int, new_phrase: str) -> JokeData:
        try:
            updated_joke = await self.repository.update_joke(
                joke_id,
                new_phrase
            )
        except (Exception, DatabaseError):
            raise JokeUpdateError('Could not update provided joke')
        return updated_joke

    async def delete_joke(self, joke_id: int):
        await self.repository.delete_joke(joke_id)

    async def get_jokes(self) -> List[Joke]:
        return await self.repository.get_jokes()

    async def least_common_multiple(
        self,
        numbers: List[int]
    ) -> LeastCommonMultiple:
        if not numbers:
            raise EmptyList('LCM array is empty, cannot make calculation')
        if len(numbers) < 2:
            raise InsufficientListSize('LCM requires minimum 2 values')

        return LeastCommonMultiple(lcm=math.lcm(*numbers))

    async def add_one_to_number(self, number: int) -> AddedNumber:
        return AddedNumber(number=number + 1)
