import unittest

from app import Buffer


class BufferTestCase(unittest.TestCase):
    def setUp(self):
        self.buffer = Buffer()

    def test_split_item(self):
        item_before = 'v1:3414:16590:119073:6af64456-8d69-4427-9c2e-32a97fe50ae3'
        item_after = ['3414', '16590', '119073', '6af64456-8d69-4427-9c2e-32a97fe50ae3']
        self.assertEqual(self.buffer._split(item_before), item_after, 'Item spliting is bad')