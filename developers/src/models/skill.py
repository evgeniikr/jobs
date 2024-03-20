from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.models.base import Base

from .card_skill_association import card_skill_association_table

if TYPE_CHECKING:
    from .card import Card


class Skill(Base):
    skill_name: Mapped[str] = mapped_column(String(32))

    cards: Mapped[list["Card"]] = relationship(
        secondary=card_skill_association_table,
        back_populates="skills",
    )
