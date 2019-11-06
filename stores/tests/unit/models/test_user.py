from models.user import UserModel
from tests.unit.unit_base_test import UnitBaseTest


class TestUser(UnitBaseTest):

    def test_create_user(self):
        user = UserModel('test username', 'test password')

        self.assertEqual(user.username, 'test username')
        self.assertEqual(user.password, 'test password')
