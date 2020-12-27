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


