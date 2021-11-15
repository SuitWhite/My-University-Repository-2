from validation import *


def is_valid(key_, value):
    return dictionary[key_](value)


class Material:
    list_of_materials = ['gold', 'silver', 'platinum']


class Type:
    list_of_types = ['rings', 'earrings', 'bracelets']


def validate_number(val):
    return is_int(val)


def validate_title(val: str):
    if val.isalpha():
        return val
    raise ValueError('Wrong title')


def validate_code(val: str):
    if len(val) != 10:
        raise ValueError('Wrong size of code')
    for i in [0, 1, 2, 3, 4, 6, 8, 9]:
        if not val[i].isnumeric():
            raise ValueError('Wrong code')
    if val[5] != '/' and val[7] != '-':
        raise ValueError('Wrong code')
    return val


def validate_material(val: str):
    for i in Material.list_of_materials:
        if i == val:
            return val
    raise ValueError('Wrong material')


def validate_type(val: str):
    for i in Type.list_of_types:
        if i == val:
            return val
    raise ValueError('Wrong material')


def validate_date_of_creation(val):
    return is_date(val)


def validate_price(val):
    return is_natural_number(val)


dictionary = {
    'id': validate_number,
    'title': validate_title,
    'code': validate_code,
    'material': validate_material,
    'type': validate_type,
    'date_of_creation': validate_date_of_creation,
    'price': validate_price
}
