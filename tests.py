from collection import *

class Tests(unittest.TestCase):

    def test_validation_true_values(self):
        jewelry_class = JEWELRY()

        try:
            jewelry_class.__setattr__("id", jewelry_class.is_valid("id","0"))
            jewelry_class.__setattr__("Title", jewelry_class.is_valid("title","Title"))
            jewelry_class.__setattr__("code", jewelry_class.is_valid("code","12344/2-34"))
            jewelry_class.__setattr__("material", jewelry_class.is_valid("material","gold"))
            jewelry_class.__setattr__("type", jewelry_class.is_valid("type","rings"))
            jewelry_class.__setattr__("date_of_creation", jewelry_class.is_valid("date_of_creation","12.12.2014"))
            jewelry_class.__setattr__("price", jewelry_class.is_valid("price","150"))
        except ValueError:
            self.fail()

        return

    def test_validation_wrong_values(self):
        jewelry_class = JEWELRY()

        try:
            jewelry_class.__setattr__("id", jewelry_class.is_valid("id","fsadf0"))
            jewelry_class.__setattr__("Title", jewelry_class.is_valid("title","Ti12 czx/c.asP@K#$tle"))
            jewelry_class.__setattr__("code", jewelry_class.is_valid("code","12344/2-34dASDadwa"))
            jewelry_class.__setattr__("material", jewelry_class.is_valid("material","golEwqd"))
            jewelry_class.__setattr__("type", jewelry_class.is_valid("type","ringFSDfdsfs"))
            jewelry_class.__setattr__("date_of_creation", jewelry_class.is_valid("date_of_creation","12DASDass.12.2014"))
            jewelry_class.__setattr__("price", jewelry_class.is_valid("price","15dasd0"))
        except ValueError:
            return

        self.fail()

    def test_validation_collection_append_true_values(self):
        jewelry_container = JewelryConteiner()
        jewelry_class = JEWELRY()
        jewelry_container.append(jewelry_class)
        if len(jewelry_container.list_) > 0:
            return
        else:
            self.fail()

    def test_validation_collection_append_wrong_values(self):
        jewelry_container = JewelryConteiner()
        not_jewelry_object = "It`s not Jewelry Class Object"
        jewelry_container.append(not_jewelry_object)
        if len(jewelry_container.list_) > 0:
            self.fail()
        else:
            return

    def test_validation_collection_wrong_id(self):
        jewelry_container = JewelryConteiner()
        jewelry_class = JEWELRY()
        jewelry_container.append(jewelry_class)
        try:
            jewelry_container.remove(500)
        except IndexError:
            return
        if len(jewelry_container.list_) > 0:
            return
        else:
            self.fail()

    def test_validation_collection_true_id(self):
        jewelry_container = JewelryConteiner()
        jewelry_class = JEWELRY()
        jewelry_container.append(jewelry_class)
        try:
            jewelry_container.remove(0)
        except IndexError:
            self.fail()
        if len(jewelry_container.list_) > 0:
            self.fail()
        else:
            return

    def test_validation_collection_true_input(self):
        jewelry_container = JewelryConteiner()
        try:
            jewelry_container.input_from_file("text_file.txt")
        except FileNotFoundError:
            self.fail()
        except FileExistsError:
            self.fail()
        return

    def test_validation_collection_true_input(self):
        jewelry_container = JewelryConteiner()
        try:
            jewelry_container.input_from_file("THIS FILE DOES NOT EXIST")
        except FileNotFoundError:
            return
        except FileExistsError:
            return
        self.fail()

    def test_validation_collection_sort(self):
        jewelry_container = JewelryConteiner()
        jewelry_container.input_from_file("text_file.txt")
        try:
            jewelry_container.sort("title")
        except ValueError:
            self.fail()
        except KeyError:
            self.fail()
        return