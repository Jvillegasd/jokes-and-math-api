from app.config.config import Config
from app.repository.interfaces.joke_api_in import IJokeApi

import aiohttp


class DadJokeAPI(IJokeApi):

    def __init__(self, session: aiohttp.ClientSession):
        config = Config()
        super().__init__(config.get('apis.dad_jokes'), session)

    async def get_random_joke(self) -> str:
        headers: dict = {
            'Accept': 'application/json'
        }
        async with self.session.get(
            f'{self.base_url}/',
            headers=headers
        ) as response:
            result: dict = await response.json()
            return result['joke']
