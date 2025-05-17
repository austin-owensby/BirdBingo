from datetime import datetime
from sqlalchemy import ARRAY, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)

class DrawHistory(Base):
    __tablename__ = "draw_history"

    name: Mapped[str]
    draw_on: Mapped[datetime]

class Board(Base):
    __tablename__ = "boards"

    owner: Mapped[str]
    grid: Mapped[list[str]] = mapped_column(ARRAY(String))
