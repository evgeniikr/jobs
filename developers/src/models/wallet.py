from sqlalchemy.orm import mapped_column, Mapped

from src.models.base import Base


class Wallet(Base):
    euro: Mapped[int] = mapped_column(default=0, server_default="0")
    dollar: Mapped[int] = mapped_column(default=0, server_default="0")
    bitcoin: Mapped[int] = mapped_column(default=0, server_default="0")
    ton: Mapped[int] = mapped_column(default=0, server_default="0")
