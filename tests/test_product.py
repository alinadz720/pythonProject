from tests.BaseCase import BaseCase
import json


class ProductTest(BaseCase):

    def test_create_valid_product(self):
        payload = json.dumps(
            {
                "productname": "apple"
            }
        )

        response = self.app.post('/product', headers={"Content-Type": "application/json"}, data=payload)
        self.assertEqual(200, response.status_code)

    def test_delete_product(self):
        payload = json.dumps(
            {
                "productname": "apple"
            }
        )
        self.app.post('/product', headers={"Content-Type": "application/json"}, data=payload)

        response = self.app.delete('/product/1')

        self.assertEqual(200, response.status_code)

    def test_update_product(self):
        self.test_create_valid_product()

        payload = json.dumps(
            {
                "username": "rvovck",
                "firstname": "roman",
                "lastname": "vovk",
                "email": "rvovck@test.com",
                "password": "1234",
                "phone": "+380380380380"
            }
        )

        token_rp = self.app.post('/user', headers={"Content-Type": "application/json"}, data=payload)

        token = token_rp.json["access_token"]

        updated_payload = json.dumps({
            "productId": 1,
            "productname": "beer",
            "status": "sold"
        })

        response = self.app.put('/product', headers={"Content-Type": "application/json",
                                                     "Authorization": "Bearer " + token},
                                data=updated_payload)

        self.assertEqual(200, response.status_code)

    def test_get_products(self):
        self.test_create_valid_product()

        response = self.app.get('/product')

        self.assertEqual(200, response.status_code)

    def test_invalid_product_inventory(self):

        response = self.app.get('/store/availability/1')

        self.assertEqual(404, response.status_code)