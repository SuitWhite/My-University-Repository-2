from validation import *


def is_valid(key_, value):
    while True:
        try:
            return dictionary[key_](value)
        except KeyError as e:
            raise ValueError('Undefined key: {}'.format(e.args[0]))


class Cities:
    list_of_cities = ['Rome', 'Paris', 'Naples', 'Vienna']


def validate_number(val):
    return is_float(val)


def validate_start_date(value):
    n = value
    n = n.split('.')
    filter(lambda x: x != '', n)
    if len(n) != 3:
        raise ValueError(str(value) + ': incorrect date')
    try:
        day = is_natural_number([n[0]])
        month = is_natural_number([n[1]])
        year = is_natural_number([n[2]])
        if day > 31 or month > 12 or year < 2020:
            raise ValueError(str(value[0]) + ': incorrect date')
    except ValueError:
        raise ValueError(str(value[0]) + ': incorrect date')
    return '.'.join([str(day), str(month), str(year)])


def validate_end_date(value):
    n = value
    n = n.split('.')
    filter(lambda x: x != '', n)
    if len(n) != 3:
        raise ValueError(str(value) + ': incorrect date')
    try:
        day = is_natural_number([n[0]])
        month = is_natural_number([n[1]])
        year = is_natural_number([n[2]])
        if day > 31 or month > 12 or year < 2020:
            raise ValueError(str(value[0]) + ': incorrect date')
    except ValueError:
        raise ValueError(str(value[0]) + ': incorrect date')
    return '.'.join([str(day), str(month), str(year)])


def validate_username(val: str):
    if val.isalpha():
        return val
    raise ValueError('Wrong title')


def validate_city(val: str):
    for i in Cities.list_of_cities:
        if i == val:
            return val
    raise ValueError('Wrong City')


dictionary = {
    'city': validate_city,
    'budget': validate_number,
    'start_date': validate_start_date,
    'end_date': validate_end_date,
    'username': validate_username,
}
