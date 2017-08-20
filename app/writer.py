from app import Database


class Writer:
    def __init__(self, name):
        self.db = Database(name)

    def write(self, item):
        try:
            if isinstance(item, list):
                pass
            else:
                return self.db.insert('''INSERT INTO cost(object_type, object_id, cost) VALUES(?, ?, ?)''',
                                      (item.resource.id, item.id, item.cost.current))
        except Exception as e:
            print(e)
