import random
from typing import (
    Dict,
    List
)

from app.repository.dad_api import DadJokeAPI
from app.repository.chuck_api import ChuckJokeAPI
from app.repository.interfaces.joke_api_in import IJokeApi
from app.repository.interfaces.repository_in import IRepository
from app.errors.repository import JokeResourceNotFound

import aiohttp


class Repository(IRepository):

    def __init__(self, session: aiohttp.ClientSession):
        dad_joke = DadJokeAPI(session=session)
        chuck_api = ChuckJokeAPI(session=session)
        joke_resources: Dict[str, IJokeApi] = {
            'Chuck': chuck_api,
            'Dad': dad_joke
        }
        super().__init__(joke_resources)

    async def get_random_joke(self) -> str:
        resources_list: List[str] = list(self.jokes_resources.keys())
        random_resource: str = random.choice(resources_list)
        return await self.jokes_resources[random_resource].get_random_joke()

    async def get_joke_from_resource(self, resource: str) -> str:
        if resource not in self.jokes_resources:
            raise JokeResourceNotFound('Provided resource not found')

        return await self.jokes_resources[resource].get_random_joke()
