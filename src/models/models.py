from pydantic import BaseModel
from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey, TIMESTAMP, DateTime
from sqlalchemy.orm import mapped_column, Mapped
from typing import List
from datetime import datetime


metaData = MetaData()

roles = Table(
    'roles',
    metaData,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=True),
    Column('permissions', List[String])

)

users = Table(
    'users',
    metaData,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('password', String, nullable=False),
    Column('role', String, nullable=True, ForeignKey = 'roles.id'), 
    Column('register_at', TIMESTAMP, default=datetime.utcnow)

)




# class Permissions():
#     __tablename__ = 'permissions'

