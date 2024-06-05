from pydantic import BaseModel
from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey, TIMESTAMP, JSON, DateTime, Numeric, CheckConstraint
from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase, DeclarativeMeta
from typing import List
from datetime import datetime


metadata = MetaData()


class Base(DeclarativeBase):
    ...


customers = Table('customers', metadata,
                  Column('id', Integer(), primary_key=True),
                  Column('first_name', String()),
                  Column('last_name', String()),
                  Column('user_name', String(), unique=True),
                  Column('email', String(), unique=True),
                  Column('address', String()),
                  Column('town', String()),
                  Column('create_on', DateTime(), default=datetime.now),
                  Column('update_on', DateTime(),
                         default=datetime.now, onupdate=datetime.now)
                  )


items = Table('items', metadata,
              Column('id', Integer(), primary_key=True),
              Column('name', String()),
              Column('cost_price', Numeric(10, 2), nullable=False),
              Column('selling_price', Numeric(10, 2), nullable=False),
              Column('quantity', Integer(), unique=True),
              CheckConstraint('quantity>0', name='quantity_check')
              )

orders = Table('orders', metadata,
               Column('id', Integer(), primary_key=True),
               Column('customer_id', ForeignKey('customers.id')),
               Column('date_placed', DateTime(), default=datetime.now),
               Column('date_shipped', DateTime())
               )


order_lines = Table('order_lines', metadata,
                    Column('id', Integer(), primary_key=True),
                    Column('order_id', ForeignKey('orders.id')),
                    Column('item_id', ForeignKey('items.id')),
                    Column('quantity', Integer())
                    )


class Users(Base):
    __tablename__ = 'users'
#     # id = Column(Integer(), primary_key=True)
#     name = Column(String(64), default='None')
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str] = mapped_column(default=datetime.now)
#     # # role:Mapped[int] = mapped_column(ForeignKey('roles.id'))
#     # register_at:Mapped[TIMESTAMP] = mapped_column(server_default=datetime.utcnow)


roles = Table(
    'roles',
    metadata,
    Column('id', Integer, primary_key=True, index=True),
    Column('name', String, nullable=True, unique=True),
    Column('permissions', JSON)
)
