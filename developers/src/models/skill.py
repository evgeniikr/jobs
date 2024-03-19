from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped

from src.models.base import Base


class Skill(Base):
    skill_name: Mapped[str] = mapped_column(String(32))
