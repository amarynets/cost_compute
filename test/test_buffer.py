import unittest

from app import Buffer, Item, Resource, Cost


class BufferTestCase(unittest.TestCase):
    def setUp(self):
        self.buffer = Buffer()

    def test_split_item(self):
        item_before = 'v1:3414:16590:119073:6af64456-8d69-4427-9c2e-32a97fe50ae3'
        item_after = ['3414', '16590', '119073', '6af64456-8d69-4427-9c2e-32a97fe50ae3']
        self.assertEqual(self.buffer._split(item_before), item_after, 'Item spliting is bad')

    def test_create_item(self):
        in_buffer = Item('3411', Resource(0, 'env'), Cost(0.0045, 0))
        self.buffer._create(in_buffer.id, in_buffer.resource, in_buffer.cost)

        self.assertEqual(self.buffer.get('3411env'), in_buffer, 'Not equals')
        self.assertEqual(self.buffer.get('6af64456-8d69-4427-9c2e-32a97fe50ae3'), None, 'Not equals')

    def test_update_item(self):
        in_buffer = Item('3411', Resource(0, 'env'), Cost(0.0045, 0))
        self.buffer._create(in_buffer.id, in_buffer.resource, in_buffer.cost)
        self.buffer._update(in_buffer, 0.005)
        self.assertEqual(self.buffer.get('3411env').cost.current, 0.0095, 'Items is difference')

    def test_serialize_item(self):
        in_buffer = Item('3411', Resource(0, 'env'), Cost(0.0045, 0))
        self.assertEqual(self.buffer._serialize(in_buffer), (0, '3411', 0.0045), 'Serialize is bad')