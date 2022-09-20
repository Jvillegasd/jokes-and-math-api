from app.schemas.joke import JokePhrase
from app.services.service import Service

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
