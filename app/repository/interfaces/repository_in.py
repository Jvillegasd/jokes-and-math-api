from typing import Dict
from abc import ABC, abstractmethod

from app.repository.interfaces.joke_api_in import IJokeApi


class IRepository(ABC):

    def __init__(self, jokes_resources: Dict[str, IJokeApi]):
        self.jokes_resources = jokes_resources

    @abstractmethod
    async def get_random_joke(self) -> str:
        """Get a random joke by choosing one from
        'jokes_resources' dict.

        Returns:
            -   str: A random joke fetched from choosed joke resource.
        """

    @abstractmethod
    async def get_joke_from_resource(self, resource: str) -> str:
        """Get a joke from choosed resource. This resource
        name needs to belong to 'joker_resources' dict keys.

        If resource is not found, an exception wil raise.

        Args:
            -   resource: str = Prefered jokes resource.

        Returns:
            -   str: A random joke fetched from provided resource.

        Exceptions:
            -   JokeResourceNotFound: This exception only raises when
            resource does not found in 'jokes_resources' dict.
        """
