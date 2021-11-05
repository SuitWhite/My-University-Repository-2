from Journey import *

class JourneyConteiner:
    list_ = []
    result_file = ""
    log_file = ""

    def __init__(self, load_from_file='', result_file='result.txt', log_file='log.txt'):
        self.result_file = result_file
        self.log_file = log_file
        if load_from_file != '':
            self.input_from_file(load_from_file)

    def __str__(self):
        s = ''
        for i in self.list_:
            s += '-' * 100 + '\n' + str(i) + '\n'
        s += '-' * 100 + '\n'
        return s

    def input_from_file(self, path='text_file.txt'):
        self.update_log_file('Load info from:\n' + str(path))
        handle = open(path)
        data = handle.readlines()  # read ALL the lines!
        handle.close()
        self.list_.clear()
        tmp_class_obj = Journey()
        for i in range(len(data)):
            if data[i].find(":") != -1:
                data[i] = data[i].split(": ")
                data[i][1] = data[i][1][0:-1]
                tmp_class_obj.__setattr__(data[i][0], tmp_class_obj.is_valid(data[i][0], data[i][1], self.log_file))
                if data[i][0] == "username":
                    self.append(tmp_class_obj)
                    tmp_class_obj = Journey()
        self.update_result_file()

    def sort(self, attr_for_sort):
        def sort_key(jewelry_object: Journey):
            return jewelry_object.dictionary_for_attr(attr_for_sort)
        self.list_.sort(key=sort_key)

    def append(self, value):
        if type(value) != Journey:
            was_error()
            return
        self.update_log_file('Add:\n' + str(value))
        self.list_.append(value)
        self.update_result_file()

    def remove(self, id):
        if is_natural_number(id) > len(self.list_):
            was_error("wrong id to remove by id", self.log_file)
            return
        del self.list_[id]

    def edit_object(self, id):
        if is_natural_number(id) > len(self.list_):
            was_error("wrong id to edit by id", self.log_file)
            return
        self.list_[id].input()

    def output(self):
        for i in self.list_:
            print(i.output())


    def update_result_file(self):
        file = open(self.result_file, 'w')
        file.write(self.__str__())
        file.close()

    def update_log_file(self, text):
        file = open(self.log_file, 'a')
        file.write('\n' + '-' * 100 + '\n' + text)
        file.close()