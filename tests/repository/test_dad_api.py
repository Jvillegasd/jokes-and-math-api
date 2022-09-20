from app.repository.dad_api import DadJokeAPI

import aiohttp
from pytest import mark
from aioresponses import aioresponses


class TestDadApi:

    @mark.asyncio
    async def test__get_random_joke(self, dad_api_response):
        session = aiohttp.ClientSession()
        api = DadJokeAPI(session)
        with aioresponses() as mocker:
            mocker.get(
                f'{api.base_url}/',
                payload=dad_api_response
            )
            random_joke = await api.get_random_joke()

            assert random_joke == dad_api_response['joke']
