from jewelry_class import *


class JewelryConteiner:
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
        tmp_class_obj = JEWELRY()
        for i in range(len(data)):
            if data[i].find(":") != -1:
                data[i] = data[i].split(": ")
                data[i][1] = data[i][1].rstrip()
                try:
                    tmp_class_obj.__setattr__(data[i][0], tmp_class_obj.is_valid(data[i][0], data[i][1], self.log_file, is_input=True))
                except KeyError as e:
                    print("Wrong file. Try again with another one.")
                    self.list_.clear()
                    validation.was_error("Key error in file: " + data[i][0] + ":" + data[i][1], self.log_file)
                    return
                except ValueError as e:
                    print("Wrong file. Try again with another one.")
                    self.list_.clear()
                    validation.was_error("Value error in file: " + data[i][0] + ":" + data[i][1], self.log_file)
                    return
                if data[i][0] == "price":
                    setattr(tmp_class_obj, "id", len(self.list_))
                    self.append(tmp_class_obj)
                    tmp_class_obj = JEWELRY()



    def sort(self, attr_for_sort):
        def sort_key(jewelry_object: JEWELRY):
            return jewelry_object.__getattribute__(attr_for_sort)

        self.list_.sort(key=sort_key)
        self.update_result_file()

    def append(self, value: JEWELRY):
        if type(value) != JEWELRY:
            validation.was_error()
            return
        setattr(value, "id", len(self.list_))
        self.update_log_file('Add:\n' + str(value))
        self.list_.append(value)
        self.update_result_file()

    def remove(self, id):
        if validation.is_int(id) > len(self.list_):
            validation.was_error("wrong id to remove by id", self.log_file)
            return
        del self.list_[int(id)]

    def edit_object(self, id):
        if validation.is_int(id) > len(self.list_):
            validation.was_error("wrong id to edit by id", self.log_file)
            return
        self.list_[id].input()

    def find_occurences(self, slovo):
        for i in range(len(self.list_)):
            if str(self.list_[i]).find(slovo) != -1:
                print(str(self.list_[i]) + '-' * 100 + '\n')
                i = i + 1

    def update_result_file(self):
        file = open(self.result_file, 'w')
        file.write(self.__str__())
        file.close()

    def update_log_file(self, text):
        file = open(self.log_file, 'a')
        file.write('\n' + '-' * 100 + '\n' + text)
        file.close()
