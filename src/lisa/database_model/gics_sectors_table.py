from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import relationship

from .base import Base


class GICS_Sectors(Base):
    __tablename__ = "GICS_Sectors"
    id = Column(Integer, primary_key=True, autoincrement=True)
    sector = Column(Text, nullable=False, unique=True)

    @classmethod
    def name(cls):
        return cls.__tablename__

    @classmethod
    def columns(cls):
        return [c.name for c in cls.__table__.columns]


# Relationships for navigation
gics_industry = relationship("GICS_Industries", back_populates="gics_sector", cascade="all, delete")
