import os
from sys import getsizeof

from app import Database, Reader, Buffer, Writer, Scanner
from const import *

db = Database('scalr.db')
db.create_table(CREATE_ENUM_TABLE)
db.create_table(CREATE_COST_TABLE)
db.insert_many(INSERT_ENUM_DATA, ENUM_DATA)


def f(row):
    meta = row['user:scalr-meta']
    meta = meta.split(':')
    if meta[0] != 'v1':
        return False
    count = 0
    for i in meta[1:]:
        if len(i) > 0:
            count += 1
    return True if count == 4 else False
reader = Reader(Scanner('/home/andrii/study/tt').get_files())
buf = Buffer()
writer = Writer(db)
for i in reader.get_data(f):
    buf.add(i)

print(buf.get('server'))

for i in buf.get_buffer(len(buf) // 4):
    writer.write(i)

print(getsizeof(buf.buffer))
