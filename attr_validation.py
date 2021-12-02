from validation import *


def is_valid(key_, value):
    decorator = dictionary[key_]

    @decorator
    def func(val):
        return value

    return func(value)



class Material:
    list_of_materials = ['gold', 'silver', 'platinum']


class Type:
    list_of_types = ['rings', 'earrings', 'bracelets']


def validate_number(func):
    def wrapper(val: int):
        return func(is_int(val))

    return wrapper


def validate_title(func):
    def wrapper(val: str):
        if val.isalpha():
            return func(val)
        raise ValueError('Wrong title')

    return wrapper


def validate_code(func):
    def wrapper(val: str):
        if len(val) != 10:
            raise ValueError('Wrong size of code')
        for i in [0, 1, 2, 3, 4, 6, 8, 9]:
            if not val[i].isnumeric():
                raise ValueError('Wrong code')
        if val[5] != '/' and val[7] != '-':
            raise ValueError('Wrong code')
        return func(val)

    return wrapper


def validate_material(func):
    def wrapper(val: str):
        for i in Material.list_of_materials:
            if i == val:
                return func(val)
        raise ValueError('Wrong material')

    return wrapper


def validate_type(func):
    def wrapper(val: str):
        for i in Type.list_of_types:
            if i == val:
                return func(val)
        raise ValueError('Wrong material')

    return wrapper


def validate_date_of_creation(func):
    def wrapper(val: str):
        return func(is_date(val))

    return wrapper


def validate_price(func):
    def wrapper(val: int):
        return func(is_natural_number(val))

    return wrapper


dictionary = {
    'id': validate_number,
    'title': validate_title,
    'code': validate_code,
    'material': validate_material,
    'type': validate_type,
    'date_of_creation': validate_date_of_creation,
    'price': validate_price
}

def decorator_function(func):
    def wrapper(obj, id='', title='', code='', material='', type='', date_of_creation='',
                 price=''):
        try:
            func(obj, id, title, code, material, type, date_of_creation,
                     price)
        except ValueError as e:
            was_error('Undefined value: {}'.format(e.args[0]), "log_file.txt")
        except KeyError as e:
            raise KeyError('Undefined key: {}'.format(e.args[0]))
    def wrapper(obj, file_for_errors='log_file.txt'):
        try:
            func(obj, file_for_errors)
        except ValueError as e:
            was_error('Undefined value: {}'.format(e.args[0]), "log_file.txt")
        except KeyError as e:
            raise KeyError('Undefined key: {}'.format(e.args[0]))
    return wrapper
