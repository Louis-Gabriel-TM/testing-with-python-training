from models.item import ItemModel
from tests.unit.unit_base_test import UnitBaseTest


class TestItem(UnitBaseTest):

    def test_create_item(self):
        # Don't have to create a StoreModel object
        # because we don't save in the database.
        item = ItemModel('test item', 19.99, 1)

        self.assertEqual(
            item.name, 'test item',
            "Custom error message is a possible 3rd argument."
        )
        self.assertEqual(item.price, 19.99)
        self.assertEqual(item.store_id, 1)
        self.assertIsNone(item.store)

    def test_item_json(self):
        item = ItemModel('test item', 19.99, 1)
        expected = {
            'name': 'test item',
            'price': 19.99
        }

        self.assertDictEqual(
            item.json(), expected,
            f"The JSON export of the item is incorrect. Received {item.json()}, expected {expected}"
        )
