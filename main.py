import traceback
from typing import (
    Dict,
    Union,
    Any,
    List
)

from app import __version__
from app.services.service import Service
from app.db.database import DataAccessLayer
from app.repository.repository import Repository
from app.schemas.joke import (
    JokeData,
    JokePhrase,
    JokeDatabase
)
from app.schemas.number import (
    AddedNumber,
    LeastCommonMultiple
)
from app.errors.repository import JokeResourceNotFound
from app.errors.service import (
    EmptyList,
    JokeUpdateError,
    InsufficientListSize
)

from fastapi import (
    FastAPI,
    HTTPException,
    status,
    Query
)
import aiohttp


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
    openapi_url='/openapi.json',
    docs_url='/docs'
)
http_joke_responses: Dict[Union[str, int], Dict[str, Any]] = {
    204: {
        'description': ''
    },
    404: {
        'description': 'Provided joke type is not found'
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


@app.get(
    '/',
    tags=['entrypoint'],
    status_code=status.HTTP_200_OK
)
async def entrypoint():
    return {'message', '🚀 @ Server is up!'}


@app.get(
    '/joke/random',
    tags=['joke'],
    response_model=JokePhrase,
    status_code=status.HTTP_200_OK,
    responses=http_joke_responses
)
async def get_random_joke():
    try:
        joke = await service.get_random_joke()
    except Exception:
        traceback.print_exc()
        raise HTTPException(
            status_code=500,
            detail=http_joke_responses[500]['description']
        )

    return joke


@app.get(
    '/joke/random/{joke_resource}',
    tags=['joke'],
    response_model=JokePhrase,
    status_code=status.HTTP_200_OK,
    responses=http_joke_responses
)
async def get_joke_from_resource(joke_resource: str):
    try:
        joke = await service.get_joke_from_resource(joke_resource)
    except JokeResourceNotFound:
        raise HTTPException(
            status_code=404,
            detail=http_joke_responses[404]['description']
        )
    except Exception:
        traceback.print_exc()
        raise HTTPException(
            status_code=500,
            detail=http_joke_responses[500]['description']
        )

    return joke


@app.post(
    '/joke',
    tags=['jokes', 'crud'],
    response_model=JokeData,
    status_code=status.HTTP_201_CREATED,
    responses=http_joke_responses
)
async def create_joke(data: JokePhrase):
    try:
        new_joke = await service.create_joke(data.phrase)
    except Exception:
        traceback.print_exc()
        raise HTTPException(
            status_code=500,
            detail=http_joke_responses[500]['description']
        )

    return new_joke


@app.patch(
    '/joke/{joke_id}',
    tags=['joke', 'crud'],
    response_model=JokeData,
    status_code=status.HTTP_200_OK,
    responses=http_joke_responses
)
async def update_joke(joke_id: int, new_phrase: JokePhrase):
    try:
        updated_joke = await service.update_joke(joke_id, new_phrase.phrase)
    except JokeUpdateError:
        traceback.print_exc()
        raise HTTPException(
            status_code=500,
            detail=http_joke_responses[500]['description']
        )

    return updated_joke


@app.delete(
    '/joke/{joke_id}',
    tags=['joke', 'crud'],
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_joke(joke_id: int):
    await service.delete_joke(joke_id)


@app.get(
    '/joke',
    tags=['joke', 'crud'],
    response_model=List[JokeDatabase],
    status_code=status.HTTP_200_OK,
    responses=http_joke_responses
)
async def get_saved_jokes():
    return await service.get_jokes()


@app.get(
    '/math/add',
    tags=['math'],
    response_model=AddedNumber,
    status_code=status.HTTP_200_OK,
    responses=http_math_responses
)
async def add_one(number: int = 0):
    try:
        result = await service.add_one_to_number(number)
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail=http_math_responses[400]['description']
        )

    return result


@app.get(
    '/math/lcm',
    tags=['math'],
    response_model=LeastCommonMultiple,
    status_code=status.HTTP_200_OK,
    responses=http_math_responses
)
async def least_common_multiple(
    numbers: List[int] = Query(default=[])
):
    try:
        lcm = await service.least_common_multiple(numbers)
    except (EmptyList, InsufficientListSize):
        raise HTTPException(
            status_code=400,
            detail=http_math_responses[400]['description']
        )

    return lcm
