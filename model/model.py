from typing import Optional

from sqlalchemy import Table, Column, create_engine
from sqlalchemy import ForeignKey, Integer, String, Unicode, Date
from sqlalchemy.orm import relationship
# from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column


class Base(DeclarativeBase):
    pass

engine = create_engine("sqlite:///model/ms.db", echo=True)
# Base = declarative_base()


class Motorcycle(Base):
    __tablename__ = 'motorcycle'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    document = Column(String(120), unique=True)
    # id: Mapped[int] = mapped_column(primary_key=True)
    # name: Mapped[str] = mapped_column(String(80), nullable=False)
    # document: Mapped[Optional[str]]


# class Client(Base):
#     __tablename__ = 'client'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(80), nullable=False)
#     surname = Column(String(80))
#     document = Column(String(120), unique=True)
#     motorcycle_id = Column(Integer, ForeignKey('motorcycle.id'), default='no')
#     motorcycle = relationship(Motorcycle)
#     birthday = Column(Date)


# Base.create_all(engine)
Base.metadata.create_all(engine, checkfirst=True)
