import sqlite3


class Database:

    def __init__(self, name):
        self.conn = sqlite3.connect(name)
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()
