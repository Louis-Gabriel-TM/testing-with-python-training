from unittest import TestCase
from post import Post


class TestPost(TestCase):

    def test_create_post(self):
        p = Post("Test", "Test Content")

        self.assertEqual(p.title, "Test")
        self.assertEqual(p.content, "Test Content")

    def test_json(self):
        p = Post("Test", "Test Content")
        expected = {
            'title': "Test",
            'content': "Test Content",
        }

        self.assertDictEqual(p.json(), expected)
