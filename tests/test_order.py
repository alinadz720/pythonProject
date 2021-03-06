from tests.BaseCase import BaseCase

import json


class OrderTest(BaseCase):

    def test_post_order(self):

        user_payload = json.dumps(
            {
                "username": "rvovck",
                "firstname": "roman",
                "lastname": "vovk",
                "email": "rvovck@test.com",
                "password": "1234",
                "phone": "+380380380380"
            }
        )

        product_payload = json.dumps(
            {
                "productname": "apple"
            }
        )

        payload = json.dumps(
            {
                "productId": 1
            }
        )

        self.app.post('/product', headers={"Content-Type": "application/json"}, data=product_payload)

        response_with_token = self.app.post('/user', headers={"Content-Type": "application/json"}, data=user_payload)

        token = response_with_token.json["access_token"]

        response_from_order = self.app.post('/order',
                                            headers=
                                            {
                                                "Content-Type": "application/json",
                                                "Authorization": "Bearer " + token
                                            },
                                            data=payload)

        self.assertEqual(200, response_from_order.status_code)

    def test_get_order(self):
        self.test_post_order()

        response = self.app.get('/store/order/1', headers={"Content-Type": "application/json"})

        self.assertEqual(200, response.status_code)

    def test_delete_order(self):
        self.test_post_order()

        response = self.app.delete('/store/order/1', headers={"Content-Type": "application/json"})

        self.assertEqual(200, response.status_code)

    def test_update_order(self):
        self.test_post_order()

        product_payload = json.dumps(
            {
                "productname": "beer"
            }
        )

        self.app.post('/product', headers={"Content-Type": "application/json"}, data=product_payload)

        payload = json.dumps({
            'userId': 1,
            'productId': 2
        })

        response = self.app.put('/store/order/1', headers={"Content-Type": "application/json"}, data=payload)

        self.assertEqual(200, response.status_code)