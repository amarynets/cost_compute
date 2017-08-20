from collections import namedtuple
from itertools import islice

Resource = namedtuple('Resource', 'id, name')
Item = namedtuple('Item', 'id, resource, cost')


class Cost:
    def __init__(self, current, in_db):
        self.current = current
        self.in_db = in_db


class Buffer:
    def __init__(self):
        self.buffer = dict()
        self.resource = [Resource(i, j) for i, j in enumerate(['env', 'farm', 'farm_role', 'server'])]

    def add(self, item):
        items = self._split(item['user:scalr-meta'])
        cost = item['Cost']
        for i, j in zip(items, self.resource):
            record = self.buffer.get(i + j.name)
            if record:
                pass
            else:
                self._create(i, j, Cost(cost, 0))

    def get(self, name):
        return self.buffer.get(name)

    def get_buffer(self, step):
        items = (self._serialize(i) for i in self.buffer.values())
        part = list(islice(items, step))
        while part:
            yield part
            part = list(islice(items, step))

    def _create(self, name, resource, cost):
        self.buffer[name + resource.name] = Item(name, resource, cost)

    def _update(self, item, cost):
        item.cost.current += cost
        self.buffer[item.id + item.resource.name] = item

    def _split(self, text):
        return text.split(':')[1:]

    def _serialize(self, item):
        return (item.resource.id, item.id, item.cost.current)