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