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
    meta = meta.split(':')[1:]
    count = 0
    for i in meta:
        if len(i) > 0:
            count += 1
    return True if count == 4 else False
reader = Reader(Scanner('/home/andrii/study/tt/cost_compute').get_files())
buf = Buffer()
writer = Writer(db)
for i in reader.get_data(f):
    buf.add(i)

print(buf.get('1farm'))

for i in buf.get_buffer(100):
    writer.write(i)

print(getsizeof(buf.buffer))
