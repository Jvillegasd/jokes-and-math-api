from app.repository.chuck_api import ChuckJokeAPI

import aiohttp
from pytest import mark
from aioresponses import aioresponses


class TestChuckApi:

    @mark.asyncio
    async def test__get_random_joke(self, chuck_api_response):
        session = aiohttp.ClientSession()
        api = ChuckJokeAPI(session)
        with aioresponses() as mocker:
            mocker.get(
                f'{api.base_url}/random',
                payload=chuck_api_response
            )
            random_joke = await api.get_random_joke()

            assert random_joke == chuck_api_response['value']
