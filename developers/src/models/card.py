from typing import TYPE_CHECKING

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.models.base import Base

if TYPE_CHECKING:
    from .user import User


class Card(Base):
    price: Mapped[int] = mapped_column()
    experience: Mapped[str] = mapped_column(String(512))
    preference: Mapped[str] = mapped_column(String(512))

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    user: Mapped["User"] = relationship(back_populates="card", uselist=False)
