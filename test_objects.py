from database_setup import *
from sqlalchemy.orm import Session
from db_credentials import *

engine = create_engine(DATABASE_CONNECTION)
Session = sessionmaker(bind=engine)
session = Session()

user1 = User(username='user1', firstname='Firstname1', lastname='Lastname1', email='1email@gmail.com', password="12345678", phone="0910345628")

product1 = Product(productname='Phone', status=ProductStatus.available)
product2 = Product(productname='TV', status=ProductStatus.available)
product3 = Product(productname='Notebook', status=ProductStatus.available)
product4 = Product(productname='MidiKeyboard', status=ProductStatus.available)
product5 = Product(productname='Monitor', status=ProductStatus.available)
product6 = Product(productname='PC', status=ProductStatus.available)
product7 = Product(productname='Headphone', status=ProductStatus.available)
product8 = Product(productname='Ebook', status=ProductStatus.available)

order1 = Order(status=OrderStatus.placed, isComplete=False, us=user1, prod=product6)

session.add(order1)

session.commit()