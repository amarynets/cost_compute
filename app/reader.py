import csv


class Reader:
    '''
    Class for return single row from file each time
    '''
    def __init__(self, filename):
        self.name = filename

    def get_data(self, criterion):
        '''
        Function for read file by criterion
        :param criterion: Function that should return True if current element must be build or False if not
        :return: next item from file that should be build
        '''
        with open(self.name, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for i in reader:
                if criterion(i):
                    yield i
                else:
                    continue
