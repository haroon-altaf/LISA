from sqlalchemy import Column, Integer, Text

from .base import Base


class NAICS_Sectors(Base):
    __tablename__ = "NAICS_Sectors"
    id = Column(Integer, primary_key=True, autoincrement=True)
    sector = Column(Text, nullable=False, unique=True)

    @classmethod
    def name(cls):
        return cls.__tablename__

    @classmethod
    def columns(cls):
        return [c.name for c in cls.__table__.columns]
