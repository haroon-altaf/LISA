from sqlalchemy import Column, ForeignKey, Integer, Text

from .base import Base


class GICS_NAICS_map(Base):
    __tablename__ = "GICS_NAICS_map"
    gics_id = Column(Integer, ForeignKey("GICS_Industries.id"), primary_key=True)
    naics_id = Column(Text, ForeignKey("NAICS_Sectors.id"), primary_key=True)

    @classmethod
    def name(cls):
        return cls.__tablename__

    @classmethod
    def columns(cls):
        return [c.name for c in cls.__table__.columns]
