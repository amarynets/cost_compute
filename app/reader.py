import csv


class Reader:
    def __init__(self, filename):
        self.name = filename

    def get_data(self, criterion):
        with open(self.name, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for i in reader:
                if criterion(i):
                    yield i
                else:
                    continue
