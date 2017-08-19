from collections import namedtuple

Cost = namedtuple('Cost', 'current, in_db')
Resource = namedtuple('Resource', 'id, name')
Item = namedtuple('Item', 'id, resource, cost')


class Buffer:
    def __init__(self):
        self.buffer = dict()
        self.resource = [Resource(i, j) for i, j in enumerate(['env', 'farm', 'farm_role', 'server'])]

    def add(self, item):
        items = self._split(item)
        cost = item['Cost']
        for i, j in zip(items, self.resource):
            record = self.buffer.get(i + j.name)
            if record:
                pass
            else:
                self._create(i + j.name, j, cost)

    def _create(self, name, resource, cost):
        self.buffer[name] = Item(name, resource, Cost(cost, 0))

    def _update(self, item, cost):
        item.cost.current += cost
        self.buffer[item.name] = item

    def _split(self, item):
        return item['user:scalr-meta'].split(':')[1:]