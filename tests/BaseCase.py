import unittest
from database_setup import Base, engine
from main import app


class BaseCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        metadata = Base.metadata
        metadata.drop_all(bind=engine)
        metadata.create_all(bind=engine)

