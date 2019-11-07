import json

from models.item import ItemModel
from models.store import StoreModel
from models.user import UserModel
from tests.base_test import BaseTest

class TestItem(BaseTest):

    def setUp(self):
        super(TestItem, self).setUp()

        with self.app() as client:
            with self.app_context():
                UserModel('test user', 'test password').save_to_db()
                auth_request = client.post(
                    '/auth', 
                    data=json.dumps({
                        'username': 'test user',
                        'password': 'test password'
                    }),
                    headers={'Content-Type': 'application/json'}
                )
                auth_token = json.loads(auth_request.data)['access_token']
                self.auth_header = f"JWT {auth_token}"

    def test_item_no_auth(self):
        with self.app() as client:
            response = client.get('/item/test')

            self.assertEqual(response.status_code, 401)

    def test_item_not_found(self):
        with self.app() as client:
            response = client.get(
                '/item/test',
                headers={'Authorization': self.auth_header}
            )

            self.assertEqual(response.status_code, 404)

    def test_item_found(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('test store').save_to_db()
                ItemModel('test item', 19.99, 1).save_to_db()
                response = client.get(
                    '/item/test%20item',
                    headers={'Authorization': self.auth_header}
                )

                self.assertEqual(response.status_code, 200)

    def test_create_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('test store').save_to_db()
                response = client.post(
                    '/item/test%20item',
                    data={'price': 19.99, 'store_id': 1}
                )

                self.assertEqual(response.status_code, 201)
                self.assertDictEqual(
                    json.loads(response.data),
                    {'name': 'test item', 'price': 19.99}
                )

    def test_create_duplicate_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('test store').save_to_db()
                ItemModel('test item', 19.99, 1).save_to_db()

                response = client.post(
                    '/item/test%20item',
                    data={'price': 19.99, 'store_id': 1}
                )

                self.assertEqual(response.status_code, 400)
                self.assertDictEqual(
                    json.loads(response.data),
                    {'message': "An item with name 'test item' already exists."}
                )

    def test_put_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('test store').save_to_db()
                response = client.put(
                    '/item/test%20item',
                    data={'price': 19.99, 'store_id': 1}
                )

                self.assertEqual(response.status_code, 200)
                self.assertDictEqual(
                    json.loads(response.data),
                    {'name': 'test item', 'price': 19.99}
                )

    def test_update_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('test store').save_to_db()
                ItemModel('test item', 19.99, 1).save_to_db()

                response = client.put(
                    '/item/test%20item',
                    data={'price': 99.99, 'store_id': 1}
                )

                self.assertEqual(response.status_code, 200)
                self.assertDictEqual(
                    json.loads(response.data),
                    {'name': 'test item', 'price': 99.99}
                )

    def test_delete_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('test store').save_to_db()
                ItemModel('test item', 19.99, 1).save_to_db()

                response = client.delete('/item/test%20item')
                self.assertEqual(response.status_code, 200)
                self.assertDictEqual(
                    json.loads(response.data),
                    {'message': "Item deleted."}
                )

    def test_item_list(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('test store').save_to_db()
                ItemModel('test item', 19.99, 1).save_to_db()

                response = client.get('/items')

                self.assertDictEqual(
                    json.loads(response.data),
                    {'items': [{'name': 'test item', 'price': 19.99}]}
                )