from unittest import TestCase

from models.item import ItemModel


class TestItem(TestCase):

    def test_create_item(self):
        item = ItemModel('test', 19.99)

        self.assertEqual(
            item.name, 'test', 
            "Custom error message is a possible 3rd argument."
        )
        self.assertEqual(item.price, 19.99)

    def test_item_json(self):
        item = ItemModel('test', 19.99)
        expected = {
            'name': 'test',
            'price': 19.99
        }

        self.assertDictEqual(
            item.json(), expected,
            f"The JSON export of the item is incorrect. Received {item.json()}, expected {expected}"
        )