import unittest

from app import Writer, Buffer
from . import create_db


class WriterTestCase(unittest.TestCase):
    def setUp(self):
        self.buffer = Buffer()
        self.writer = Writer(':memory:')
        self.writer.db = create_db(self.writer.db)
        self.buffer.add({'Cost': 0.0045, 'user:scalr-meta': 'v1:3414:16590:119073:6af64456-8d69-4427-9c2e-32a97fe50ae3'})
        self.buffer.add({'Cost': 0.01, 'user:scalr-meta': 'v1:32:3453:22342:34dfrg56-8d69-4427-9c2e-32a97fe50ae3'})

    def test_first_write_to_db(self):
        item = self.buffer.get('32env')
        last_id = self.writer.write(item)
        self.assertTrue(isinstance(last_id, int), 'Not return int')
        self.assertEqual(last_id, 1, 'DB not returned id')
        item = self.buffer.get('3414env')
        last_id = self.writer.write(item)
        self.assertEqual(last_id, 2, 'DB not returned id')