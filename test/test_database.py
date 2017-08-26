import unittest

from app import Database

from . import create_db


class DBTestCase(unittest.TestCase):
    def setUp(self):
        self.db = create_db(Database(':memory:'))

    def test_insert_one(self):
        r = self.db.run('''INSERT INTO cost(object_type, object_id, cost) VALUES(?, ?, ?)''', (0, '3414', 0.55))
        self.assertEqual(r, 1, 'Not correct id')