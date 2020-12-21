import sys
from sqlalchemy import Column, ForeignKey, Integer, String, MetaData, Boolean, Enum, orm
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
<<<<<<< Updated upstream
    id = Column(Integer, primary_key=True)
    username = Column(String(64))
    firstname = Column(String(64))
    lastname = Column(String(64))
    email = Column(String(64))
    password = Column(String(64))
    phone = Column(String(64))

=======
    userId = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True)
    firstname = Column(String(50))
    lastname = Column(String(50))
    email = Column(String(50))
    password = Column(String(50))
    phone = Column(String(50))
>>>>>>> Stashed changes

class Product(Base):
    __tablename__ = 'Products'

    productId = Column(Integer, primary_key=True, autoincrement=True)
    productname = Column(String(50))
    status = Column(Enum(ProductStatus))


class Order(Base):
    __tablename__ = 'Orders'
<<<<<<< Updated upstream
    id = Column(Integer, primary_key=True)
    userId = Column(Integer, ForeignKey('Users.id'))
    user = relationship('Users')
    productId = Column(Integer, ForeignKey('Products.id'))
    product = relationship('Products')
    status = Column(Enum(OrderStatus))
    is_complete = Column(Boolean, unique=False, default=False)
=======
    orderId = Column(Integer, primary_key=True, autoincrement=True)
    userId = Column(Integer, ForeignKey('Users.userId'))
    productId = Column(Integer, ForeignKey('Products.productId'))
    status = Column(Enum(OrderStatus))
    isComplete = Column(Boolean, default=False)
    us = orm.relationship(User, foreign_keys=[userId], backref='adinfo_from', lazy='joined')
    prod = orm.relationship(Product, foreign_keys=[productId], backref='adinfo_from', lazy='joined')

Base.metadata.create_all(engine)
>>>>>>> Stashed changes
