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
    userId = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True)
    firstname = Column(String(50))
    lastname = Column(String(50))
    email = Column(String(50))
    password = Column(String(250))
    phone = Column(String(50))


class Product(Base):
    __tablename__ = 'Products'

    productId = Column(Integer, primary_key=True, autoincrement=True)
    productname = Column(String(50))
    status = Column(Enum(ProductStatus))

    def __init__(self, productname):
        self.productname = productname
        self.status = ProductStatus.available

class Order(Base):
    __tablename__ = 'Orders'
    orderId = Column(Integer, primary_key=True, autoincrement=True)
    userId = Column(Integer, ForeignKey('Users.userId'))
    productId = Column(Integer, ForeignKey('Products.productId'))
    status = Column(Enum(OrderStatus))
    isComplete = Column(Boolean, default=False)
    us = orm.relationship(User, foreign_keys=[userId], backref='adinfo_from', lazy='joined')
    prod = orm.relationship(Product, foreign_keys=[productId], backref='adinfo_from', lazy='joined')

    def __init__(self, User, Product):
        self.userId = User.userId
        self.productId = Product.productId
        self.status = OrderStatus.placed

Base.metadata.create_all(engine)
