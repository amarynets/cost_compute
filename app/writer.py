
class Writer:
    def __init__(self, database):
        self.db = database

    def write(self, item):
        try:
            if isinstance(item, list):
                return self.db.insert_many('''INSERT INTO cost(object_type, object_id, cost) VALUES(?, ?, ?)''',
                                    (item))
            else:
                return self.db.insert('''INSERT INTO cost(object_type, object_id, cost) VALUES(?, ?, ?)''',
                                      (item.resource.id, item.id, item.cost))
        except Exception as e:
            print(e)
