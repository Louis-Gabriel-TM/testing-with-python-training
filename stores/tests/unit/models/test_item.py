from unittest import TestCase

from models.item import ItemModel
from models.store import StoreModel


class TestItem(TestCase):

    def test_create_item(self):
        StoreModel('test store').save_to_db()
        item = ItemModel('test item', 19.99, 1)

        self.assertEqual(
            item.name, 'test item',
            "Custom error message is a possible 3rd argument."
        )
        self.assertEqual(item.price, 19.99)
        self.assertEqual(item.store_id, 1)

    def test_item_json(self):
        StoreModel('test store').save_to_db()
        item = ItemModel('test item', 19.99, 1)
        expected = {
            'name': 'test item',
            'price': 19.99
        }

        self.assertDictEqual(
            item.json(), expected,
            f"The JSON export of the item is incorrect. Received {item.json()}, expected {expected}"
        )
