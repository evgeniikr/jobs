from sqlalchemy import Table, Column, ForeignKey, Integer, UniqueConstraint

from .base import Base

card_skill_association_table = Table(
    "card_skill_association",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("card_id", ForeignKey("cards.id"), nullable=False),
    Column("skill_id", ForeignKey("skills.id"), nullable=False),
    UniqueConstraint("card_id", "skill_id", name="idx_unique_card_skill"),
)
