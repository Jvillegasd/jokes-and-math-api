from typing import (
    Dict,
    Union,
    Any
)

from app import __version__
from app.services.service import Service
from app.db.database import DataAccessLayer
from app.repository.repository import Repository

from fastapi import (
    FastAPI
    # HTTPException,
    # Request,
    # status
)
import aiohttp


BASE_PATH: str = '/api/v1'
description: str = """
SquadMakers test API
Get jokes from 3rd party APIs and manages them,
apply some math operations over a list of numbers
or a single one.
"""
app: FastAPI = FastAPI(
    title='SquadMakers test API',
    description=description,
    version=__version__,
    contact={
        'name': 'Johnny Villegas',
        'email': 'johnnyvillegaslrs@gmail.com'
    },
    openapi_url=f'{BASE_PATH}/openapi.json',
    docs_url=f'{BASE_PATH}/docs'
)
http_joke_responses: Dict[Union[str, int], Dict[str, Any]] = {
    204: {
        'description': ''
    },
    400: {
        'description': 'Provided joke type is not allowed at the moment'
    },
    500: {
        'description': 'Something went wrong...'
    }
}
http_math_responses: Dict[Union[str, int], Dict[str, Any]] = {
    400: {
        'description': 'A valid umber or list of number not provided'
    },
    500: {
        'description': 'Something went wrong...'
    }
}

dal = DataAccessLayer()
session: aiohttp.ClientSession = aiohttp.ClientSession()
repository = Repository(
    session=session,
    postgres_conn=dal.database
)
service = Service(repository)


@app.on_event('startup')
async def startup():
    await dal.database.connect()


@app.on_event('shutdown')
async def shutdown():
    await dal.database.disconnect()
    await session.close()
