import json

from models.user import UserModel
from tests.base_test import BaseTest


class TestUser(BaseTest):

    def test_register_user(self):
        with self.app() as client:
            with self.app_context():
                request = client.post(
                    '/register',
                    data={
                        'username': 'test username',
                        'password': 'test password'
                    }
                )

                self.assertEqual(request.status_code, 201)
                self.assertIsNotNone(
                    UserModel.find_by_username('test username')
                )
                self.assertDictEqual(
                    json.loads(request.data),
                    {'message': "User created successfully."}
                )

    def test_register_and_login(self):
        pass

    def test_register_duplicate_user(self):
        pass
