class JokeUpdateError(Exception):
    """When joke update statement fails"""


class EmptyList(Exception):
    """When a LCM list comes empty."""


class InsufficientListSize(Exception):
    """When a LCM list size is less than required by operation"""
