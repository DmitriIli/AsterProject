from pydantic import BaseModel
from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey, TIMESTAMP, DateTime, JSON
from sqlalchemy.orm import mapped_column, Mapped
from typing import List
from datetime import datetime


metadata = MetaData()

roles = Table(
    'roles',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=True),
    Column('permissions', JSON)

)

users = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('password', String, nullable=False),
    Column('role', String, nullable=True, ForeignKey = 'roles.id'), 
    Column('register_at', TIMESTAMP, default=datetime.utcnow),
    Column('role_id', Integer, ForeignKey('roles.id'))
)




# class Permissions():
#     __tablename__ = 'permissions'

