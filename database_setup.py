import sys
from sqlalchemy import Column, ForeignKey, Integer, String, MetaData, Boolean, Enum
from sqlalchemy.ext.declarative import declarative_base
import enum

from sqlalchemy.orm import relationship, sessionmaker, scoped_session

from sqlalchemy import create_engine

from db_credentials import *

engine = create_engine(DATABASE_CONNECTION)

metadata = MetaData(engine)
Base = declarative_base(metadata)


class OrderStatus(enum.Enum):
    placed = "placed"
    approved = "approved"
    delivered = "delivered"


class ProductStatus(enum.Enum):
    available = "available"
    pending = "pending"
    sold = "sold"


class User(Base):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True)
    username = Column(String(64))
    firstname = Column(String(64))
    lastname = Column(String(64))
    email = Column(String(64))
    password = Column(String(64))
    phone = Column(String(64))


class Product(Base):
    __tablename__ = 'Products'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    status = Column(Enum(ProductStatus))


class Order(Base):
    __tablename__ = 'Orders'
    id = Column(Integer, primary_key=True)
    userId = Column(Integer, ForeignKey('Users.id'))
    user = relationship('Users')
    productId = Column(Integer, ForeignKey('Products.id'))
    product = relationship('Products')
    status = Column(Enum(OrderStatus))
    is_complete = Column(Boolean, unique=False, default=False)
