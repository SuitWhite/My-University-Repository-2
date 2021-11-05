import os
import date_functions


def is_str(value: []):
    return value[0]


def is_natural_number(value: []):
    n = value[0]
    n = n.strip()
    if not (is_int([n]) and int(n) > 0):
        raise ValueError(n + ' не є натуральним цілим числом')
    return int(n)


def is_menu(value: []):
    n = value[0]
    n = n.strip()
    if not n in value[1]:
        raise ValueError(n + ' не є полем меню')
    return n


def is_greater_then(value: []):
    n = value[0]
    k = is_int(n)
    for i in value:
        if k <= i:
            raise ValueError(str(k) + ' не є більшим за ' + str(i))
    return k


def is_in_list(value: []):
    n = value[0]
    n = is_natural_number([n])
    list_ = value[1]
    if not n in list_:
        raise ValueError(str(n) + ' немає в потрібному масиві')
    return n


def is_attribute(value: []):
    n = value[0]
    att = value[1]
    try:
        return n.__getattribute__(att)
    except Exception:
        raise ValueError("Object has no attr " + str(att))


def has_attribute(value: []):
    try:
        is_attribute([value[1], value[0]])
        return value[0]
    except Exception as error:
        raise ValueError(error)


def is_valid_array(value: []):
    n = value[0]
    s = []
    if value[2] == -1:
        s = n.split(value[3])
    else:
        s = n.split(value[3])[:value[2]]
        if len(s) < value[2]:
            raise ValueError(str(s) + ': не правильна кількість елементів')
    for i in range(len(s)):
        s[i].strip()
        s[i] = value[1](s[i])
    return s





def is_date_in_range(value: []):
    if not date_functions.comparison(value[1], value[0]) or not date_functions.comparison(value[0], value[2]):
        raise ValueError(str(value[0]) + ' : некоректна дата')
    return value[0]


def is_file(value: []):
    n = value[0]
    n = n.strip()
    if not os.path.isfile(n):
        raise ValueError(str(n) + ': файлу не існує, або програма його не бачить')
    return n


def is_vaccine_filed(value: []):
    return value[1](value[2], value[0], is_input=True)




def input_validation(text="", additional_condition=is_str, *value_for_conditional):
    slesh_n = '\n'
    print(text, end=f'{slesh_n if text != "" else ""}')
    while True:
        try:
            a = [input()]
            a += value_for_conditional
            return additional_condition(a)
        except ValueError as error:
            print(error)
            print('спробуйте йще раз')
        except KeyboardInterrupt:
            print('Програма завершила свою роботу')
            exit()


def was_error(message='error', file=''):
    message = str(message)
    message = '\n' + '*' * len(message) + '\n' + message + '\n' + '*' * len(message)
    print(message)
    if file != '':
        file = open(file, 'a')
        file.write('\n' + message + '\n')
        file.close()


def array_input(text="", size=-1, additional_condition=is_str, split_symbol=' '):
    list_ = input_validation(text, is_valid_array, additional_condition, size, split_symbol)
    if size != -1:
        list_ = list_[:size]
    return list_

def is_float(value):
    n = value
    n = n.strip()
    try:
        return float(n)
    except ValueError:
        raise ValueError(n + ' не є дійсним числом')


def is_int(value: []):
    if len(value) == 0:
        value = ['None']
    n = value[0]
    if type(n) == str:
        n = n.strip()
    try:
        return int(n)
    except ValueError:
        raise ValueError(n + ' is not int')