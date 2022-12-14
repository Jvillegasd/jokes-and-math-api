from sqlalchemy import (
    Column,
    Integer,
    DateTime,
    String
)
from sqlalchemy.sql import func
from app.db.database import Base


class Joke(Base):
    __tablename__ = 'joke'
    joke_id = Column(Integer, primary_key=True, index=True)
    phrase = Column(String)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(
        DateTime,
        server_default=func.now(),
        server_onupdate=func.now()
    )

    def __repr__(self) -> str:
        return f'<Joke(id={self.joke_id}, phrase={self.phrase})>'
