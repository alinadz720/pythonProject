import json
from tests.BaseCase import BaseCase


class CreateUserTest(BaseCase):

    def test_create_valid_user(self):
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

        response = self.app.post('/user', headers={"Content-Type": "application/json"}, data=payload)

        self.assertEqual(200, response.status_code)

    def test_update_user(self):
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

        updated_payload = json.dumps(
            {
                "username": "rvovck",
                "email": "rvovck@test.com",
                "password": "12345",
            })

        response = self.app.put('/user', headers={"Content-Type": "application/json",
                                                  "Authorization": "Bearer " + token},
                                data=updated_payload)

        self.assertEqual(200, response.status_code)
