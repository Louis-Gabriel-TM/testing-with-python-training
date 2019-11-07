import json

from models.item import ItemModel
from models.store import StoreModel
from tests.base_test import BaseTest


class TestStore(BaseTest):

    def test_create_store(self):
        with self.app() as client:
            with self.app_context():
                response = client.post('/store/test%20store')

                self.assertEqual(response.status_code, 201)
                self.assertIsNotNone(StoreModel.find_by_name('test store'))
                self.assertDictEqual(
                    json.loads(response.data),
                    {'name': 'test store','items': []}
                )

    def test_create_duplicate_store(self):
        with self.app() as client:
            with self.app_context():
                client.post('/store/test_store')
                response = client.post('/store/test_store')

                self.assertEqual(response.status_code, 400)

    def test_store_not_found(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('test store').save_to_db()
                response = client.get('/store/test%20store')

                self.assertEqual(response.status_code, 200)
                self.assertDictEqual(
                    json.loads(response.data),
                    {'name': 'test store', 'items': []}
                )

    def test_store_found(self):
        with self.app() as client:
            with self.app_context():
                response = client.get('/store/test%20store')

                self.assertEqual(response.status_code, 404)
                self.assertDictEqual(
                    json.loads(response.data),
                    {'message': "Store not found."}
                )

    def test_store_with_items_found(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('test store').save_to_db()
                ItemModel('test item', 19.99, 1).save_to_db()
                response = client.get('/store/test%20store')

                self.assertEqual(response.status_code, 200)
                self.assertDictEqual(
                    json.loads(response.data),
                    {'name': 'test store', 'items': [
                        {'name': 'test item','price': 19.99}
                    ]}
                )

    def test_store_list(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('test store').save_to_db()

                response = client.get('/stores')
                self.assertDictEqual(
                    json.loads(response.data),
                    {'stores': [
                        {'name': 'test store', 'items': []}
                    ]}
                )

    def test_store_with_items_list(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('test store').save_to_db()
                ItemModel('test item', 19.99, 1).save_to_db()

                response = client.get('/stores')
                self.assertDictEqual(
                    json.loads(response.data),
                    {'stores': [
                        {'name': 'test store', 'items': [
                            {'name': 'test item', 'price': 19.99}
                        ]}
                    ]}
                )

    def test_delete_store(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('test_store').save_to_db()
                response = client.delete('/store/test_store')

                self.assertEqual(response.status_code, 200)
                self.assertDictEqual(
                    json.loads(response.data),
                    {'message': "Store deleted."}
                )