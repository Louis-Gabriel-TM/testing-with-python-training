from unittest import TestCase

from app import app
from db import db


class IntegrationBaseTest(TestCase):
    """
    This class is the parent class to each non-unit test.
    It allows the instantiation of the database dynamically
    and makes sure that it is a new blank database each time.
    """

    def setUp(self):
        # Make sure the database exists
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
        with app.app_context():
            db.init_app(app)
            db.create_all()

        # Get a test client
        self.app = app.test_client()
        self.app_context = app.app_context

    def tearDown(self):
        # Insure the database is blank
        with app.app_context():
            db.session.remove()
            db.drop_all()
