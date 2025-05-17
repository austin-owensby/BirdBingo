from datetime import datetime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)

class DrawHistory(Base):
    __tablename__ = "draw_history"

    name: Mapped[str]
    draw_on: Mapped[datetime]