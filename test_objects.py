from database_setup import *

session = Session()

user1 = User(userId=1, username='user1', firstname='Firstname1', lastname='Lastname1', email='1email@gmail.com',
             password="12345678", phone="0910345628")
user2 = User(userId=2, username='user2', firstname='Firstname2', lastname='Lastname2', email='2email@gmail.com',
             password="12325278", phone="0920347238")
user3 = User(userId=3, username='user3', firstname='Firstname3', lastname='Lastname3', email='3email@gmail.com',
             password="12545678", phone="0937395628")

product1 = Product(productId=1, name='Phone', status=ProductStatus.available)
product2 = Product(productId=2, name='TV', status=ProductStatus.available)
product3 = Product(productId=3, name='Notebook', status=ProductStatus.available)
product4 = Product(productId=4, name='MidiKeyboard', status=ProductStatus.available)
product5 = Product(productId=5, name='Monitor', status=ProductStatus.available)
product6 = Product(productId=6, name='PC', status=ProductStatus.available)
product7 = Product(productId=7, name='Headphone', status=ProductStatus.available)
product8 = Product(productId=8, name='Ebook', status=ProductStatus.available)

#order1 = Order(orderId=1, userdId=1, productId=1, status=OrderEnum.placed, is_complete=False, from_user=1, to_product=1)
#order2 = Order(orderId=2, userdId=2, productId=3, status=OrderEnum.placed, is_complete=False, from_user=2, to_product=3)

session.add(user1)
session.add(user2)
session.add(user3)

session.add(product1)
session.add(product2)
session.add(product3)
session.add(product4)
session.add(product5)
session.add(product6)
session.add(product7)
session.add(product8)

#session.add(order1)
#session.add(order2)

session.commit()
