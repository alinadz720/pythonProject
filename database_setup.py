import sys
from sqlalchemy import Column, ForeignKey, Integer, String, MetaData, Boolean, orm
from sqlalchemy.ext.declarative import declarative_base
import enum

from sqlalchemy.orm import relationship, sessionmaker, scoped_session

from sqlalchemy import create_engine
from sqlalchemy.testing.schema import Table

engine = create_engine('postgresql://postgres:1887@localhost:5432/postgres')
SessionNw = sessionmaker(bind=engine)
Session = scoped_session(SessionNw)

#cursor = engine.cursor()

Base = declarative_base()


class OrderEnum(enum.Enum):
    placed = "placed"
    approved = "approved"
    delivered = "delivered"


class ProductStatus(enum.Enum):
    available = "available"
    pending = "pending"
    sold = "sold"


class User(Base):
    __tablename__ = 'users'
    userId = Column(Integer, primary_key=True)
    username = Column(String(64))
    firstname = Column(String(64))
    lastname = Column(String(64))
    email = Column(String(64))
    password = Column(String(64))
    phone = Column(String(64))


class Product(Base):
    __tablename__ = 'products'

    productId = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    status = Column(String(16))


class Order(Base):
    __tablename__ = 'orders'
    orderId = Column(Integer, primary_key=True)
    userId = Column(Integer, ForeignKey('User.userId'))
    productId = Column(Integer, ForeignKey('Product.productId'))
    status = Column(String(16))
    is_complete = Column(Boolean, unique=False, default=False)

    #from_user = orm.relationship(User,  backref='adinfo_from', lazy='joined')
    #to_product = orm.relationship(Product,  backref='adinfo_froms', lazy='joined')

#Base.metadata.create_all(engine)