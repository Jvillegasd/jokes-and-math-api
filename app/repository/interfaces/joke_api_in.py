from abc import ABC, abstractmethod


class IJokeApi(ABC):

    def __init__(self, base_url: str):
        self.base_url = base_url

    @abstractmethod
    async def get_random_joke(self) -> str:
        """Just get a random joke from defined endpoint.

        Returns:
            -   str: Random joke.
        """
