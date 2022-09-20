from app.config.config import Config
from app.repository.interfaces.joke_api_in import IJokeApi

import aiohttp


class ChuckJokeAPI(IJokeApi):

    def __init__(self, session: aiohttp.ClientSession):
        config = Config()
        super().__init__(config.get('apis.chuck_norris'), session)

    async def get_random_joke(self) -> str:
        headers: dict = {
            'Content-Type': 'application/json'
        }
        async with self.session.get(
            f'{self.base_url}/random',
            headers=headers
        ) as response:
            result: dict = await response.json()
            return result['value']
