from unittest import TestCase

from app import app
from db import db


class BaseTest(TestCase):
    """
    This class is the parent class to each non-unit test.
    It allows the instantiation of the database dynamically
    and makes sure that it is a new blank database each time.
    """

    SQLALCHEMY_DATABASE_URI = 'sqlite:///'

    @classmethod
    def setUpClass(cls):  # Run once for all the tests in a test class
        app.config['SQLALCHEMY_DATABASE_URI'] = cls.SQLALCHEMY_DATABASE_URI
        app.config['DEBUG'] = False
        app.config['PROPAGATE_EXCEPTIONS'] = True

        with app.app_context():
            db.init_app(app)

    def setUp(self):  # Run once per test
        # Make sure the database exists
        with app.app_context():
            db.create_all()

        # Get a test client
        self.app = app.test_client
        self.app_context = app.app_context

    def tearDown(self):
        # Insure the database is blank
        with app.app_context():
            db.session.remove()
            db.drop_all()
