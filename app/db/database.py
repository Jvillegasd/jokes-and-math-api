from app.config.config import Config

import databases
from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base

config = Config()
Base = declarative_base(
    metadata=MetaData(schema=config.get('postgres.schema'))
)


class DataAccessLayer:

    def __init__(self):
        __database_url: str = (
            'postgresql://{}:{}@{}:{}/{}'.format(
                config.get('postgres.user'),
                config.get('postgres.password'),
                config.get('postgres.host'),
                config.get('postgres.port'),
                config.get('postgres.db_name')
            )
        )
        self.database: databases.Database = databases.Database(__database_url)
