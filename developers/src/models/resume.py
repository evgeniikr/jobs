from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped
from fastapi import UploadFile

from src.models.base import Base


class Resume(Base):
    file: Mapped[bytes] = mapped_column(nullable=False)
    total_experience: Mapped[int] = mapped_column(default=0, server_default="0")
