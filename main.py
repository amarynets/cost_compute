from app import Database, Reader


from const import *

db = Database('scalr.db')
db.create_table(CREATE_ENUM_TABLE)
db.create_table(CREATE_COST_TABLE)
db.insert_many(INSERT_ENUM_DATA, ENUM_DATA)

reader = Reader('aws0.csv')

def f(row):
    meta = row['user:scalr-meta']
    meta = meta.split(':')[1:]
    if any(len(i) > 0 for i in meta):
        return True
    else:
        return False
count = 0
for i in reader.get_data(f):
    count += 1
    print(i)
print(count)