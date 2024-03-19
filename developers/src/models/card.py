from typing import TYPE_CHECKING, List

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.models.base import Base
from .card_skill_association import card_skill_association_table

if TYPE_CHECKING:
    from .user import User
    from .skill import Skill


class Card(Base):
    price: Mapped[int] = mapped_column()
    experience: Mapped[str] = mapped_column(String(1024))
    preference: Mapped[str] = mapped_column(String(512))

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    user: Mapped["User"] = relationship(back_populates="card", uselist=False)

    skills: Mapped[List["Skill"]] = relationship(
        secondary=card_skill_association_table,
        back_populates="cards",
    )
