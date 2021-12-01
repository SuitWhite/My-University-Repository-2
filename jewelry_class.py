import attr_validation
import validation


class JEWELRY:
    id: int = ''
    title: str = ''
    code: str = ''
    material: str = ''
    type: str = ''
    date_of_creation: str = ''
    price: int = ''
    __attributes = ['id', 'title', 'code', 'material', 'type', 'date_of_creation',
                    'price']

    @attr_validation.decorator_function
    def __init__(self, id='', title='', code='', material='', type='', date_of_creation='',
                 price=''):
        if id == '':
            return
        arguments = locals()
        for key, value in arguments.items():
            self.__setattr__(key, value)

    def get_attr(self, name_of_attr, file_for_errors=''):
        try:
            return self.__getattribute__(name_of_attr)
        except KeyError as e:
            raise validation.was_error(e, file_for_errors)

    @attr_validation.decorator_function
    def input(self, file_for_errors='log_file.txt'):
        for i in self.__attributes:
            self.__setattr__(i, self.is_valid(i, input('Enter ' + i + ': '), is_input=True))


    def output(self):
        data = []
        for i in self.__attributes:
            text = i + ': ' + self.__getattribute__(i) + '\n'
            data.append(text)
        return data

    @attr_validation.decorator_function
    def read_from_file(self, path='text_file.txt'):
        handle = open(path, "r")
        data = handle.readlines()  # read ALL the lines!
        handle.close()
        for i in range(len(data)):
            if data[i].find(":") != -1:
                data[i] = data[i].split(": ")
                data[i][1] = data[i][1].rstrip()
                self.__setattr__(data[i][0], self.is_valid(data[i][0], data[i][1]))

    def has_value(self, value):
        for i in [a for a in dir(self) if not ('__' in a) and not callable(getattr(self, a))]:
            if self.__getattribute__(i) == value:
                return True
        return False


    def is_valid(self, name, val, log_file='log_file.txt', is_input=False):
        try:
            return attr_validation.is_valid(name, val)
        except ValueError as error:
            if is_input:
                raise ValueError(error)
            validation.was_error(error, log_file)

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