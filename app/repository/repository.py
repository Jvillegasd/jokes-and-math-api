import random
from typing import (
    Dict,
    List
)

from app.models.joke import Joke
from app.schemas.joke import JokeData
from app.repository.dad_api import DadJokeAPI
from app.repository.chuck_api import ChuckJokeAPI
from app.repository.interfaces.joke_api_in import IJokeApi
from app.repository.interfaces.repository_in import IRepository
from app.errors.repository import JokeResourceNotFound

import aiohttp
from sqlalchemy import (
    select,
    insert,
    delete,
    update
)
from sqlalchemy.orm import Session


class Repository(IRepository):

    def __init__(
        self,
        postgres_conn: Session,
        session: aiohttp.ClientSession,
    ):
        dad_joke = DadJokeAPI(session=session)
        chuck_api = ChuckJokeAPI(session=session)
        joke_resources: Dict[str, IJokeApi] = {
            'Chuck': chuck_api,
            'Dad': dad_joke
        }
        super().__init__(joke_resources, postgres_conn)

    async def get_random_joke(self) -> str:
        resources_list: List[str] = list(self.jokes_resources.keys())
        random_resource: str = random.choice(resources_list)
        return await self.jokes_resources[random_resource].get_random_joke()

    async def get_joke_from_resource(self, resource: str) -> str:
        if resource not in self.jokes_resources:
            raise JokeResourceNotFound('Provided resource not found')

        return await self.jokes_resources[resource].get_random_joke()

    async def create_joke(self, phrase: str) -> JokeData:
        query = insert(Joke).values(phrase=phrase)
        last_record_id = await self.postgres_conn.execute(query)
        return JokeData(
            number=last_record_id,
            phrase=phrase
        )

    async def update_joke(
        self,
        joke_id: int,
        new_joke_phrase: str
    ) -> JokeData:
        query = (
            update(Joke).
            where(Joke.joke_id == joke_id).
            values(phrase=new_joke_phrase)
        )
        await self.postgres_conn.execute(query)
        return JokeData(
            number=joke_id,
            phrase=new_joke_phrase
        )

    async def delete_joke(self, joke_id: int):
        query = (
            delete(Joke).
            where(Joke.joke_id == joke_id)
        )
        await self.postgres_conn.execute(query)

    async def get_jokes(self) -> List[Joke]:
        query = select(Joke)
        results = await self.postgres_conn.fetch_all(query)
        return results
