import sqlite3


class Database:

    def __init__(self, name):
        try:
            self.conn = sqlite3.connect(name)
            self.cursor = self.conn.cursor()
        except Exception as e:
            print(e)

    def __del__(self):
        self.conn.close()

    def create_table(self, query):
        try:
            self.cursor.execute(query)
        except Exception as e:
            print(e)

    def insert(self, query, param):
        try:
            self.cursor.execute(query, param)
            self.conn.commit()
            return self.cursor.lastrowid
        except Exception as e:
            print(e)

    def insert_many(self, query, param):
        try:
            for i, item in enumerate(param):
                self.cursor.execute(query, item)
                if i % 1000 == 0:
                    self.conn.commit()
            self.conn.commit()
            return self.cursor.lastrowid
        except Exception as e:
            print(e)
