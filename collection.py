from jewelry_class import *
from abc import ABC, abstractmethod
from copy import deepcopy

class Memento(ABC):
    """
    The Memento interface provides a way to retrieve the memento's metadata,
    such as creation date or name. However, it doesn't expose the Originator's
    state.
    """

    @abstractmethod
    def get_list(self) -> list:
        pass



class JewelryConteiner:
    result_file = ""
    log_file = ""

    def __init__(self, load_from_file='', result_file='result.txt', log_file='log.txt'):
        self.result_file = result_file
        self.log_file = log_file
        self.list_ = []
        if load_from_file != '':
            self.input_from_file(load_from_file)

    def __init__(self, LIST: list) -> None:
        self.list_ = LIST

    def __init__(self) -> None:
        self.result_file = 'result.txt'
        self.log_file = 'log.txt'
        self.list_ = []

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

    def save(self) -> Memento:
        """
        Saves the current state inside a memento.
        """

        return ConcreteMemento(self.list_)

    def restore(self, memento: Memento) -> None:
        """
        Restores the Originator's state from a memento object.
        """

        self.list_ = deepcopy(memento.get_list())
        self.update_result_file()


class ConcreteMemento(Memento):
    def __init__(self, listj) -> None:
        self.list_ = deepcopy(listj)

    def get_list(self) -> list:
        """
        The Originator uses this method when restoring its state.
        """
        return self.list_


class Caretaker():
    """
    The Caretaker doesn't depend on the Concrete Memento class. Therefore, it
    doesn't have access to the originator's state, stored inside the memento. It
    works with all mementos via the base Memento interface.
    """

    def __init__(self, originator: JewelryConteiner) -> None:
        self._mementos = []
        self._mementosreundo = []
        self._originator = originator

    def backup(self) -> None:
        self._mementos.append(self._originator.save())

    def undo(self) -> None:
        if not len(self._mementos):
            return

        self._mementosreundo.append(self._originator.save())
        memento = self._mementos.pop()
        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()

    def reundo(self) -> None:
        if not len(self._mementosreundo):
            return

        self._mementos.append(self._originator.save())
        memento = self._mementosreundo.pop()
        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()

    def show_history(self) -> None:
        print("Caretaker: Here's the list of mementos:")
        for memento in self._mementos:
            print(memento.get_name())