from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.models.base import Base

if TYPE_CHECKING:
    from .card import Card


class Resume(Base):
    file: Mapped[bytes] = mapped_column(nullable=False)
    total_experience: Mapped[int] = mapped_column(default=0, server_default="0")

    card_id: Mapped[int] = mapped_column(ForeignKey("cards.id"))
    card: Mapped["Card"] = relationship(back_populates="resume")
