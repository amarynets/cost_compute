CREATE_ENUM_TABLE = '''CREATE TABLE IF NOT EXISTS enum 
(id integer PRIMARY KEY AUTOINCREMENT,
 name VARCHAR(10) NOT NULL,
 UNIQUE(id, name)
 );'''

CREATE_COST_TABLE = '''CREATE TABLE IF NOT EXISTS cost
(id INTEGER PRIMARY KEY AUTOINCREMENT, 
object_type INTEGER, 
object_id VARCHAR(32), 
cost REAL,
FOREIGN KEY (object_type) REFERENCES enum (id)
)
'''
INSERT_ENUM_DATA = 'INSERT OR IGNORE INTO enum(id, name) VALUES(?, ?)'
ENUM_DATA = [(0, 'env'), (1, 'farm'), (2, 'farm_role'), (3, 'server')]


def create_db(db):
    db.create_table(CREATE_ENUM_TABLE)
    db.create_table(CREATE_COST_TABLE)
    db.run_many(INSERT_ENUM_DATA, (ENUM_DATA))
    return db
