from collection import *


def menu():
    jewelry_collection = JewelryConteiner()
    str_bound = "*************************************************************"
    str_bound2 = "============================================================="
    text = "0 - exit\n"
    text += "1 - read objects from file into container\n"
    text += "2 - write container objects to file\n"
    text += "3 - add new object to container\n"
    text += "4 - remove object from container by its id\n"
    text += "5 - edit object in container and/or file by its id\n"
    text += "6 - show container's content\n"
    text += "7 - find occurences of your search query in collection\n"
    text += "8 - sort collection\n"
    text += str_bound
    text += "\nEnter your option >>> "

    while True:
        print(text)
        option = validation.is_int(input())
        if option == 0:
            break
        elif option == 1:
            jewelry_collection.input_from_file() # default text_file.txt
        elif option == 2:
            if len(jewelry_collection.list_) > 0:
                jewelry_collection.update_result_file()
            else:
                print("\n--- there is no objects in container ---\n")
        elif option == 3:
            print("Enter new object:\n")
            jewelry_object = JEWELRY()
            jewelry_object.input()
            jewelry_collection.append(jewelry_object)
        elif option == 4:
            id = input("Enter id of the object you want to remove >>> ")
            jewelry_collection.remove(id)
        elif option == 5:
            id = input("Enter id of the object you want to edit >>> ")
            jewelry_collection.edit_object(id)
        elif option == 6:
            print(str(jewelry_collection))
        elif option == 7:
            search_query = input("Enter what info you want to find in container >>> ")
            jewelry_collection.find_occurences(search_query)
            print(str_bound)
        elif option == 8:
            attr = input("Enter attribute to sort >>> ")
            jewelry_collection.sort(attr)
        else:
            print("\n--- wrong option ---\n")
        print(str_bound2)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    menu()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
