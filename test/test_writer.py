import unittest

from app import Writer, Buffer, Database
from . import create_db


class WriterTestCase(unittest.TestCase):
    def setUp(self):
        self.buffer = Buffer()
        self.writer = Writer(Database(':memory:'))
        self.writer.db = create_db(self.writer.db)
        self.buffer.add({'Cost': 0.0045, 'user:scalr-meta': 'v1:3414:16590:119073:6af64456-8d69-4427-9c2e-32a97fe50ae3'})
        self.buffer.add({'Cost': 0.01, 'user:scalr-meta': 'v1:32:3453:22342:34dfrg56-8d69-4427-9c2e-32a97fe50ae3'})

    def test_write_to_db(self):
        item = self.buffer.get('32env')
        self.writer.write(item.serialize())

    def test_update_db(self):
        item = self.buffer.get('32env')
        self.writer.write([item.serialize()])
        self.writer.write([item.serialize()])
        self.writer.db.run('''SELECT object_type, object_id FROM cost WHERE object_type=0 and object_id='32' ''')
        in_db = self.writer.db.cursor.fetchall()
        self.assertEqual(in_db, [(0, '32')])
