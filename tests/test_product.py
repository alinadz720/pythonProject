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
