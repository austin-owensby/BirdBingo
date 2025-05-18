from datetime import datetime
import os
from sqlalchemy import ARRAY, String
from sqlalchemy.sql import func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import create_engine

DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL is None:
    # If developing locally, follow the README to add it
    raise Exception("Could not find a DATABASE_URL environmental variable.")

engine = create_engine(DATABASE_URL)

def get_engine():
    return engine

class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class DrawHistory(Base):
    __tablename__ = "draw_history"

    name: Mapped[str]
    draw_on: Mapped[datetime] = mapped_column(default=func.now())
    user: Mapped[str] = mapped_column(server_default="Unknown")

class Board(Base):
    __tablename__ = "boards"

    owner: Mapped[str]
    grid: Mapped[list[str]] = mapped_column(ARRAY(String))
