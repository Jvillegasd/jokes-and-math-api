from app.config.config import Config

import databases
from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base

# Naming convention for Alembic
# https://alembic.sqlalchemy.org/en/latest/naming.html
naming_convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
Base = declarative_base(
    metadata=MetaData(naming_convention=naming_convention)
)
config = Config()


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
