from app.repository.interfaces.joke_api_in import IJokeApi

import aiohttp


class DadJokeAPI(IJokeApi):

    def __init__(self, base_url: str, session: aiohttp.ClientSession):
        super().__init__(base_url, session)

    async def get_random_joke(self) -> str:
        async with self.session.get(f'{self.base_url}/') as response:
            result: dict = await response.json()
            return result['joke']
