from tests.BaseCase import BaseCase

import json


class LoginTest(BaseCase):

    def test_invalid_login(self):

        payload = json.dumps(
            {
                "username": "usr",
                "password": "123"
            }
        )

        response = self.app.get('/login', headers={"Content-Type": "application/json"}, data=payload)

        self.assertEqual(404, response.status_code)

    def test_successful_login(self):

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

        self.app.post('/user', headers={"Content-Type": "application/json"}, data=payload)

        login_payload = json.dumps(
            {
                "username": "rvovck",
                "password": "1234"
            }
        )

        response = self.app.get('/login', headers={"Content-Type": "application/json"}, data=login_payload)

        self.assertEqual(200, response.status_code)

