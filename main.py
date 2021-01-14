from flask import Flask, request, abort, jsonify
from wsgiref.simple_server import make_server

from sqlalchemy.orm import sessionmaker

from database_setup import *
from schemas import UserSchema, ProductSchema
from flask_bcrypt import Bcrypt
from marshmallow import ValidationError
from flask_jwt_extended import JWTManager, jwt_required, jwt_optional, create_access_token, get_jwt_identity

DBSession = sessionmaker(bind=engine)

session = DBSession()

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config['JWT_SECRET_KEY'] = '12345678'
jwt = JWTManager(app)


@app.route('/user', methods=['POST', 'PUT'])
@jwt_optional
def register_user():
    data = request.json
    if request.method == 'POST':
        user_data = {'username': data['username'], 'firstname': data['firstname'], 'lastname': data['lastname'],
                     'email': data['email'],
                     'password': bcrypt.generate_password_hash(data['password']).decode('utf-8'),
                     'phone': data['phone']}
        user_reply = session.query(User).filter(User.username == data['username']).one_or_none()
        if user_reply is None:
            user = UserSchema().load(user_data)
            session.add(user)
            session.commit()
        else:   # pragma: no cover
            return "This username is not available"

        token = create_access_token(identity=user.username)
        return jsonify(access_token=token), 200

    if request.method == 'PUT':

        if not get_jwt_identity():  # pragma: no cover
            abort(401, 'You need to log in')

        user = session.query(User).filter(User.username == data['username']).one_or_none()

        if user.username != get_jwt_identity():   # pragma: no cover
            abort(403, 'You can only change your own account details')

        username = data['username']
        password = bcrypt.generate_password_hash(data['password']).decode('utf-8')

        email = data['email']

        if user is None:   # pragma: no cover
            abort(404, 'User does not exist')
        else:
            user.username = username
            user.password = password
            user.email = email
            session.add(user)
            session.commit()
            token = create_access_token(identity=username)
            return jsonify(access_token=token), 200


@app.route('/login')
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if not username:
        return jsonify({"msg": "Missing username parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    user = session.query(User).filter(User.username == username).one_or_none()

    if not user:
        abort(404, 'User does not exist')

    if bcrypt.check_password_hash(user.password, password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return abort(403, 'Invalid password')


@app.route('/product', methods=['POST', 'PUT', 'GET'])
@jwt_optional
def create_update_product():
    data = request.json
    if request.method == 'POST':
        newProduct = Product(data['productname'])
        newProduct.status = ProductStatus.available
        session.add(newProduct)
        session.commit()
        return f"Product {newProduct.productname} successfully created!"
    if request.method == 'PUT':
        product_id = data['productId']
        product_name = data['productname']
        product_status = data['status']
        product = session.query(Product).filter(Product.productId == product_id).one_or_none()

        if product is None:
            abort(404)
        else:
            product.status = product_status
            product.name = product_name
            session.add(product)
            session.commit()
            return f"Product {product_id} successfully modified"
    if request.method == 'GET':
        products = session.query(Product).all()

        schema = ProductSchema(many=True)
        response = schema.dump(products)

        response_dict = {i: response[i] for i in range(0, len(response))}

        return response_dict
    return '200'


@app.route('/product/<id>', methods=['DELETE'])
def delete_product(id):
    product = session.query(Product).filter(Product.productId == id).one_or_none()
    order = session.query(Order).filter(Order.productId == id).first()
    if product is None:
        abort(404, 'Product not found')
    while order:   # pragma: no cover
        session.delete(order)
        session.commit()
        order = session.query(Order).filter(Order.productId == id).one_or_none()

    session.delete(product)
    session.commit()
    return f"Product {product.productname}({id}) successfully deleted"


@app.route('/store/availability/<id>')
def check_product_inventory(id):
    product = session.query(Product).filter(Product.productId == id).one_or_none()
    if product is None:
        abort(404, 'Product not found')
    return f"Product {product.productname} is {product.status.value}"


@app.route('/order', methods=['POST'])
@jwt_optional
def place_order():
    data = request.json
    if not get_jwt_identity():
        abort(401, 'You need to log in')
    try:
        user = session.query(User).filter(User.username == get_jwt_identity()).one_or_none()
        product = session.query(Product).filter(Product.productId == data['productId']).one_or_none()
        if user is None or product is None:   # pragma: no cover
            abort(404, 'User or product not found')
    except ValidationError:   # pragma: no cover
        return abort(400, 'Bad request')

    order = Order(user, product)

    session.add(order)
    session.commit()
    return f"Order was successfully placed!"


@app.route('/store/order/<id>', methods=['GET', 'PUT', 'DELETE'])
def single_order(id):
    order = session.query(Order).filter(Order.orderId == id).one_or_none()
    if order is None:
        abort(404)

    if request.method == 'GET':
        response = f'Order for {order.prod.productname} has been placed by {order.us.username}. '
        response += f'It\'s status is {order.status.value}. '
        if order.isComplete:
            response += "It's already completed"
        else:
            response += "It has not yet been completed"
        return response

    if request.method == 'DELETE':
        session.delete(order)
        session.commit()
        return f'Order {id} has been successfully deleted'

    if request.method == 'PUT':
        data = request.json
        user = session.query(User).filter(User.userId == data['userId']).one_or_none()
        product = session.query(Product).filter(Product.productId == data['productId']).one_or_none()
        if user is None or product is None:
            abort(404)
        order.user = user
        order.product = product
        session.add(order)
        session.commit()
        return f'Order {id} has been successfully modified'

    return '200'


@app.route('/api/v1/hello-world-6')
def hello():  # pragma: no cover
    return 'Hello World 6'


if __name__ == '__main__':  # pragma: no cover
    server = make_server('', 8000, app)
    print('http://127.0.0.1:8000/api/v1/hello-world-6')
    server.serve_forever()


