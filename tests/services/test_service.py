import math
from typing import List

from app.schemas.joke import JokePhrase
from app.services.service import Service
from app.schemas.number import (
    LeastCommonMultiple,
    AddedNumber
)
from app.errors.service import (
    EmptyList,
    InsufficientListSize
)
from app.errors.service import JokeUpdateError

import pytest
from pytest import mark


class TestService:

    async def some_joke(self):
        return 'some joke'

    @mark.asyncio
    async def test__get_joke_from_resource(self, mocker):
        repo_mock = mocker.Mock()
        repo_mock.get_joke_from_resource.return_value = self.some_joke()

        res: str = 'some joke res'
        service = Service(repo_mock)
        result = await service.get_joke_from_resource(res)

        assert type(result) == JokePhrase
        assert result.phrase == await self.some_joke()

    @mark.asyncio
    async def test__update_joke_fail(self, mocker):
        repo_mock = mocker.Mock()
        repo_mock.update_joke.side_effect = JokeUpdateError
        service = Service(repo_mock)

        some_joke_id: int = 1
        some_phrase: str = 'testing'
        with pytest.raises(JokeUpdateError):
            await service.update_joke(some_joke_id, some_phrase)

    @mark.asyncio
    async def test__lcm(self, mocker):
        repo_mock = mocker.Mock()
        service = Service(repo_mock)

        numbers: List[int] = [1, 2, 3, 4]
        expected_lcm: int = math.lcm(*numbers)

        result = await service.least_common_multiple(numbers)
        assert type(result) == LeastCommonMultiple
        assert result.lcm == expected_lcm

    @mark.asyncio
    async def test__lcm_insufficient_size_fail(self, mocker):
        repo_mock = mocker.Mock()
        service = Service(repo_mock)

        numbers: List[int] = [1]
        with pytest.raises(InsufficientListSize):
            await service.least_common_multiple(numbers)

    @mark.asyncio
    async def test__lcm_empty_list_fail(self, mocker):
        repo_mock = mocker.Mock()
        service = Service(repo_mock)

        numbers: List[int] = []
        with pytest.raises(EmptyList):
            await service.least_common_multiple(numbers)

    @mark.asyncio
    async def test__add_one_to_number(self, mocker):
        repo_mock = mocker.Mock()
        service = Service(repo_mock)

        number: int = 1
        result = await service.add_one_to_number(number)
        assert type(result) == AddedNumber
        assert result.number == number + 1
