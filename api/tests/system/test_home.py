import json
from unittest import TestCase

from app import app


class TestHome(TestCase):

    def test_home(self):
        with app.test_client() as c:
            response = c.get('/')

            self.assertEqual(response.status_code, 200)
            self.assertEqual(
                json.loads(response.get_data()),
                {'message': "Hello world!"}
            )
