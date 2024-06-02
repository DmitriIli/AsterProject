from pydantic import BaseModel
from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey, TIMESTAMP, JSON
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy.ext.declarative import declarative_base
from typing import List
from datetime import datetime

from database import Base




class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer(), primary_key=True)
    name = Column(String(64), default='None')
    # id:Mapped[int] = mapped_column(primary_key=True)
    # username:Mapped[str] = mapped_column(unique=True)
    # password:Mapped[str] 
    # # role:Mapped[int] = mapped_column(ForeignKey('roles.id'))
    # register_at:Mapped[TIMESTAMP] = mapped_column(server_default=datetime.utcnow)

metadata = MetaData()

roles = Table(
    'roles',
    metadata,
    Column('id', Integer, primary_key=True, index=True),
    Column('name', String, nullable=True, unique=True),
    Column('permissions', JSON)
)
