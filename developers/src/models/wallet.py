import uuid
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.models.base import Base

if TYPE_CHECKING:
    from .user import User


class Wallet(Base):
    euro: Mapped[int] = mapped_column(default=0, server_default="0")
    dollar: Mapped[int] = mapped_column(default=0, server_default="0")
    bitcoin: Mapped[int] = mapped_column(default=0, server_default="0")
    ton: Mapped[int] = mapped_column(default=0, server_default="0")

    user_id: Mapped[uuid] = mapped_column(ForeignKey("users.id"))

    user: Mapped["User"] = relationship(back_populates="wallet", uselist=False)
