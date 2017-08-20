import csv
import os


class Reader:
    '''
    Class for return single row from file each time
    '''
    def __init__(self, files):
        self.files = files

    def read(self, name, criterion):
        '''
        Function for read file by criterion
        :param criterion: Function that should return True if current element must be build or False if not
        :param name: name of file
        :return: next item from file that should be build
        '''
        with open(name, 'r') as csvfile:
            print('Reading data from {}'.format(name))
            reader = csv.DictReader(csvfile)
            for i in reader:
                if criterion(i):
                    yield i
                else:
                    continue

    def get_data(self, criterion):
        for i in self.files:
            yield from self.read(i, criterion)


class Scanner:
    def __init__(self, path):
        self.path = path
        self.files = list()
        self.build_file_list()
        print('Directory is scanned')

    def build_file_list(self):
        if os.path.isfile(self.path):
            self.files.append(self.path)
        else:
            self.scan_dir()

    def scan_dir(self):
        for root, dirs, files in os.walk(self.path):
            for file in files:
                if file.endswith('.csv'):
                    self.files.append(os.path.join(root, file))

    def get_files(self):
        return self.files
