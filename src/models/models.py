from pydantic import BaseModel
from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey, TIMESTAMP, JSON
from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase, DeclarativeMeta
from typing import List
from datetime import datetime


class Base(DeclarativeBase):
    ...


class Users(Base):
    __tablename__ = 'users'
#     # id = Column(Integer(), primary_key=True)
#     name = Column(String(64), default='None')
    id:Mapped[int] = mapped_column(primary_key=True)
    username:Mapped[str] = mapped_column(unique=True)
    password:Mapped[str] = mapped_column(default=datetime.now)
#     # # role:Mapped[int] = mapped_column(ForeignKey('roles.id'))
#     # register_at:Mapped[TIMESTAMP] = mapped_column(server_default=datetime.utcnow)

metadata = MetaData()

roles = Table(
    'roles',
    metadata,
    Column('id', Integer, primary_key=True, index=True),
    Column('name', String, nullable=True, unique=True),
    Column('permissions', JSON)
)
