from collections import namedtuple
from itertools import islice

Resource = namedtuple('Resource', 'id, name')


class Item:
    def __init__(self, id, resource, cost):
        self.id = id
        self.resource = resource
        self.cost = cost

    def __str__(self):
        return self.__dict__

    def serialize(self):
        return (self.resource.id, self.id, self.cost)


class Buffer:
    def __init__(self):
        self.buffer = dict()
        self.resource = [Resource(i, j) for i, j in enumerate(['env', 'farm', 'farm_role', 'server'])]

    def __len__(self):
        return len(self.buffer)

    def add(self, item):
        items = self._split(item['user:scalr-meta'])
        cost = item['Cost']
        for i, j in zip(items, self.resource):
            record = self.buffer.get(i + j.name)
            if record:
                self._update(record, cost)
            else:
                self._create(i, j, cost)

    def get(self, name):
        return self.buffer.get(name)

    def get_buffer(self, step):
        items = (i.serialize() for i in self.buffer.values())
        part = list(islice(items, step))
        while part:
            yield part
            part = list(islice(items, step))

    def _create(self, name, resource, cost):
        self.buffer[name + resource.name] = Item(name, resource, float(cost))

    def _update(self, item, cost):
        item.cost += float(cost)
        self.buffer[item.id + item.resource.name] = item

    def _split(self, text):
        return text.split(':')[1:]

