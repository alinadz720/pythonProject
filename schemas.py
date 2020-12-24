from marshmallow import Schema, fields, post_load
from database_setup import User, Product, Order


class UserSchema(Schema):
#    userId = fields.Int()
    username = fields.Str()
    firstname = fields.Str()
    lastname = fields.Str()
    email = fields.Str()
    password = fields.Str()
    phone = fields.Str()

    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)


class ProductSchema(Schema):
    productId = fields.Int()
    productname = fields.Str()
    status = fields.Str()


class OrderSchema(Schema):
    orderId = fields.Int()
    userId = fields.Int()
    productId = fields.Int()
    status = fields.Str()
    is_complete = fields.Bool()
