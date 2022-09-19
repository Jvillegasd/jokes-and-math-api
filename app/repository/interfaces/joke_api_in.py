from abc import ABC, abstractmethod

import aiohttp


class IJokeApi(ABC):

    def __init__(self, base_url: str, session: aiohttp.ClientSession):
        self.base_url = base_url
        self.session = session

    @abstractmethod
    async def get_random_joke(self) -> str:
        """Just get a random joke from defined endpoint.

        Returns:
            -   str: Random joke.
        """
