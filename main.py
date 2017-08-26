from multiprocessing import Process, Queue
from sys import getsizeof, argv
import time

from app import Database, Reader, Buffer, Writer, Scanner
from const import *

db = Database('scalr.db')
db.create_table(CREATE_ENUM_TABLE)
db.create_table(CREATE_COST_TABLE)
db.run_many(INSERT_ENUM_DATA, ENUM_DATA)


def time_duration(func):
    def wraps(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print('Duration', time.time() - start)
    return wraps


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


def make_file_list(path):
    return Scanner(path).get_files()


def single_thread(files, queue=None):
    reader = Reader(files)
    buf = Buffer()

    for i in reader.get_data(f):
        buf.add(i)

    if queue:
        queue.put(buf)


@time_duration
def multi(files):
    queue = Queue()
    print(files)
    process = [Process(target=single_thread, args=(i, queue)).start() for i in files]

    writer = Writer(db)
    for i in range(len(process)):
        buffer = queue.get()
        for j in buffer.get_buffer(len(buffer) // 4):
            print('Writing to DB from buffer {}'.format(i))
            writer.write(j)


if __name__ == '__main__':
    path = argv[1]
    multi(make_file_list(path))
