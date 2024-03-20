import uuid
from typing import TYPE_CHECKING

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.models.base import Base

from .card_skill_association import card_skill_association_table

if TYPE_CHECKING:
    from .user import User
    from .skill import Skill
    from .resume import Resume


class Card(Base):
    price: Mapped[int] = mapped_column(default=0, server_default="0")
    experience: Mapped[str] = mapped_column(String(1024))
    preference: Mapped[str] = mapped_column(String(512))

    user_id: Mapped[uuid] = mapped_column(ForeignKey("users.id"))

    user: Mapped["User"] = relationship(back_populates="card", uselist=False)

    skills: Mapped[list["Skill"]] = relationship(
        secondary=card_skill_association_table,
        back_populates="cards",
    )

    resume: Mapped[list["Resume"]] = relationship(back_populates="card")
