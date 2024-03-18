from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.models.base import Base


class User(Base):
    username: Mapped[str] = mapped_column(
        String(32),
        unique=True,
    )
