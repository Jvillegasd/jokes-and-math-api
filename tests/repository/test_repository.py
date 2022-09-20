from typing import List

from app.schemas.joke import JokeData
from app.repository.repository import Repository
from app.errors.repository import JokeResourceNotFound

import pytest
import aiohttp
from pytest import mark


class TestRepository:

    async def last_record_id(self):
        return 1

    async def some_jokes(self) -> List[dict]:
        return [
            {'joke_id': 1, 'phrase': 'joke 1'},
            {'joke_id': 2, 'phrase': 'joke 2'}
        ]

    @mark.asyncio
    async def test__get_joke_from_resource_fail(self, mocker):
        session = aiohttp.ClientSession()
        postgres_conn = mocker.Mock()
        repo = Repository(postgres_conn, session)

        unknown_joke_res: str = 'Just a unknown resource'
        with pytest.raises(JokeResourceNotFound):
            await repo.get_joke_from_resource(unknown_joke_res)

    @mark.asyncio
    async def test__create_joke(self, mocker):
        session = aiohttp.ClientSession()
        postgres_conn = mocker.Mock()
        postgres_conn.execute.return_value = self.last_record_id()

        expected_value: str = 'a random joke'
        repo = Repository(postgres_conn, session)
        result = await repo.create_joke(expected_value)

        assert type(result) == JokeData
        assert result.number == await self.last_record_id()
        assert result.phrase == expected_value

    @mark.asyncio
    async def test__update_joke(self, mocker):
        session = aiohttp.ClientSession()
        postgres_conn = mocker.Mock()
        postgres_conn.execute.return_value = self.last_record_id()

        expected_value: str = 'a random joke'
        repo = Repository(postgres_conn, session)
        result = await repo.update_joke(
            await self.last_record_id(),
            expected_value
        )

        assert type(result) == JokeData
        assert result.number == await self.last_record_id()
        assert result.phrase == expected_value

    @mark.asyncio
    async def test__get_jokes(self, mocker):
        session = aiohttp.ClientSession()
        postgres_conn = mocker.Mock()
        postgres_conn.fetch_all.return_value = self.some_jokes()

        expected_value: List[dict] = await self.some_jokes()
        repo = Repository(postgres_conn, session)
        result = await repo.get_jokes()

        assert type(result) == list
        assert len(result) > 0
        assert len(result) == len(expected_value)
        assert result[0].phrase == expected_value[0]['phrase']
