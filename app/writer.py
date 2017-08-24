
class Writer:
    def __init__(self, database):
        self.db = database
        self.type = {k: list() for k in range(4)}

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

    def _is_in_db(self, item):
        if item[1] in self.type[0]:
            return True
        else:
            return False
