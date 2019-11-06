from models.item import ItemModel
from models.store import StoreModel
from tests.integration.integration_base_test import IntegrationBaseTest


class TestItem(IntegrationBaseTest):

    def test_crud(self):
        with self.app_context():
            StoreModel('test store').save_to_db()
            item = ItemModel('test item', 19.99, 1)

            self.assertIsNone(
                ItemModel.find_by_name('test item'),
                f"Found an item with name {item.name}, but expected not to."
            )
            item.save_to_db()
            self.assertIsNotNone(ItemModel.find_by_name('test item'))
            item.delete_from_db()
            self.assertIsNone(ItemModel.find_by_name('test item'))

    def test_store_relationship(self):
        with self.app_context():
            store = StoreModel('test store')
            item = ItemModel('test item', 19.99, 1)

            store.save_to_db()
            item.save_to_db()

            self.assertEqual(item.store.name, 'test store')
