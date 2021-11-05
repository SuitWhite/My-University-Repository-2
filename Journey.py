from attr_validation import *
from validation import *

import datetime

class Journey:
    city: str = ''
    budget: float = ''
    start_date: datetime.date = ''
    end_date: datetime.date = ''
    username: str = ''
    __attributes = ['city', 'budget', 'start_date', 'end_date', 'username']
    dictionary_for_attr = {
        'city': city,
        'budget': budget,
        'start_date': start_date,
        'end_date': end_date,
        'username': username,
    }

    def __init__(self, city='Rome', budget='2.12', start_date='5.1.2021', end_date='5.1.2021', username='UsrName'):
        for i in vars().items():
            if i[0] != 'self':
                self.__setattr__(i[0], self.is_valid(i[0], i[1]))

    def get_attr(self, name_of_attr, file_for_errors=''):
        try:
            return self.dictionary_for_attr[name_of_attr]
        except KeyError as e:
            raise was_error(e, file_for_errors)

    def input(self, file_for_errors=''):
        for i in self.__attributes:
            self.__setattr__(i, self.is_valid(i, input('Enter ' + i + ': ')))

    def output(self):
        data = []
        for i in self.__attributes:
            text = i + ': ' + self.dictionary_for_attr[i] + '\n'
            data.append(text)
        return data

    def read_from_file(self, path='text_file.txt'):
        handle = open(path, "r")
        data = handle.readlines()  # read ALL the lines!
        handle.close()
        for i in range(len(data)):
            if data[i].find(":") != -1:
                data[i] = data[i].split(": ")
                self.__setattr__(data[i][0], self.is_valid(data[i][0], data[i][1]))


    def has_value(self, value):
        for i in [a for a in dir(self) if not ('__' in a) and not callable(getattr(self, a))]:
            if self.__getattribute__(i) == value:
                return True
        return False

    def is_valid(self, name, val, log_file='log_file.txt', is_input=False):
        try:
            return is_valid(name, val)
        except ValueError as error:
            if is_input:
                raise ValueError(error)
            was_error(error, log_file)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        s = ''
        for i in self.__attributes:
            s += i + ': ' + self.get_attr_str(i) + '\n'
        s = s[:-1]
        return s

    def get_attr_str(self, name, file=''):
        ans = self.get_attr(name, file)
        if ans is not None:
            ans = str(ans)
        return ans

    def get_attr_names(self):
        return self.__attributes