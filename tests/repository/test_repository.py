from app.repository.repository import Repository
# from app.errors.repository import JokeResourceNotFound
from app.schemas.joke import JokeData

# import pytest
import aiohttp
from pytest import mark


class TestRepository:

    async def last_record_id(self):
        return 1

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
