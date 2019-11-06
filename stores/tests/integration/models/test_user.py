from models.user import UserModel
from tests.base_test import BaseTest


class TestUser(BaseTest):

    def test_crud(self):
        with self.app_context():
            user = UserModel('test username', 'test password')

            self.assertIsNone(UserModel.find_by_username('test username'))
            self.assertIsNone(UserModel.find_by_id(1))

            user.save_to_db()

            self.assertIsNotNone(UserModel.find_by_username('test username'))
            self.assertIsNotNone(UserModel.find_by_id(1))
