# Jokes and Maths!

This is a [SquadMakers](https://squadmakers.com) Backend test for Python. It consists in create a FastAPI with TDD (Unit testing) for handle Jokes CRUD, 3rd party APIs integrations for get random jokes depending on the selected resource and handle some Maths operations (LCM and Addition).


## How to run

This project is Dockerized, so you will not be worried about dependencies. Just make sure you have `docker` and `docker-compose` installed in your device.
To run the project for the first time, you will need to write this command down on your bash:

    docker-compose up -d --build
    docker exec -it api-jokes alembic upgrade head

## Dockerized

As mentioned in the previous section, this project is dockerized. In the `docker-compose.yml` file you notice that `FastAPI API` and a `PostgreSQL image` was configured in order to run the project.

## Migrations

`Alembic` library was used for migration tracking. So, when you run the project for the first time, you will need to run migrations in order to populate PostgreSQL container. To do that, just run the following command after the project is up:

    docker exec -it api-jokes alembic upgrade head

## API documentation

FastAPI instagrates `Swagger` for documentation. You can access by going to the following URL:

    /docs
    
    ex:
    http://localhost:4002/docs
    

## Environment

This is how the Environment variables file looks like:

    CHUCK_JOKES_API=
    DAD_JOKES_API=
    POSTGRES_HOST=
    POSTGRES_PORT=
    POSTGRES_USER=
    POSTGRES_PASSWORD=
    POSTGRES_DB_NAME=
    API_PORT=
For the sake of the test, the `.env` file will be tracked in the repository.

## Pre-commit hooks

This project implement `pre-commit` library. This library allows you to run validations before commits or pushes.
Here, `MyPy`, `Flake8` and `Pytest` hooks were configured to run before any `commit` or `push`.


## UML diagrams

UML class diagram created by [Mermaid](https://mermaidjs.github.io/). 

```mermaid
classDiagram

IRepository  -->  IJokeApi

Repository  --|>  IRepository

DadApiJoke  --|>  IJokeApi

ChuckJokeAPI  --|>  IJokeApi

Service  --|>  IService

IService  -->  IRepository

Main  -->  IService

Main  -->  DataAccessLayer

Main  -->  JokeDatabase

Main  -->  JokeResources

IRepository  -->  Joke

IRepository  -->  JokeData

IRepository  -->  JokePhrase

  

class  IRepository  {

<<Interface>>

+jokes_resources:  List[str, IJokeApi]

+postgres_conn:  sqlalchemy.orm.Session

  

+get_random_joke()  str

+get_joke_from_resource(resource:  str)  str

+create_joke(phrase:  str)  JokeData

+update_joke(joke_id:  int, new_phrase:  str)  JokeData

+delete_joke(joke_id:  int)

+get_jokes()  List(Joke)

}

class  IJokeApi  {

<<Interface>>

+base_url  str

+session aiohttp.ClientSession

  

+get_random_joke()  str

}

class  DadApiJoke  {

<<Class>>

}

class  ChuckJokeAPI  {

<<Class>>

}

class  Repository  {

<<Class>>

}

class  IService  {

<<Interface>>

+repository IRepository

  

+get_random_joke()  JokePhrase

+get_joke_from_resource(resource:  str)  JokePhrase

+create_joke(phrase:  str)  JokeData

+update_joke(joke_id:  int, new_phrase:  str)  JokeData

+delete_joke(joke_id:  int)

+get_jokes()  List(Joke)

+least_common_multiple(numbers:  List[int])  LeastCommonMultiple

+add_one_to_number(number:  int)  AddedNumber

}

class  Service  {

<<Class>>

}

class  DataAccessLayer  {

+database:  databases.Database

}

class  Main  {

<<Class>>

+dal:  DataAccessLayer

+session:  aiohttp.ClientSession

+service:  IService

  

+startup()

+shutdown()

+entrypoint() Dict(str, str)

+get_random_joke()  JokePhrase

+get_joke_from_resource(joke_resource: JokeResources)  JokePhrase

+create_joke(data: JokePhrase)  JokeData

+update_joke(joke_id: int, new_phrase: JokePhrase)  JokeData

+delete_joke(joke_id:  int)

+get_saved_jokes()  List(JokeDatabase)

+least_common_multiple(numbers: List[int] = Query(default=[])  LeastCommonMultiple

+add_one(number: int = 0)  AddedNumber

}

class  Joke  {

<<SQLalchemy model>>

  

+joke_id:  int

+phrase:  str

+created_at:  datetime

+updated_at:  datetime

}

class  JokeData  {

<<Pydantic model>>

  

+number:  int

+phrase:  str

}

class  JokePhrase  {

<<Pydantic model>>

  

+phrase:  str

}

class  JokeDatabase  {

<<Pydantic model>>

  

+joke_id:  int

+phrase:  str

+created_at:  datetime

+updated_at:  datetime

}

class  JokeResources  {

<<enumeration>>

  

dad

chuck

}
```