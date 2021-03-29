# 3. Написать декоратор для логирования типов позиционных аргументов функции, например:
# def type_logger...
#     ...
#
#
# @type_logger
# def calc_cube(x):
#    return x ** 3
#
# >>> a = calc_cube(5)
# 5: <class 'int'>
# Примечание: если аргументов несколько - выводить данные о каждом через запятую;
# можете ли вы вывести тип значения функции?
# Сможете ли решить задачу для именованных аргументов?
# Сможете ли вы замаскировать работу декоратора?
# Сможете ли вывести имя функции, например, в виде:
# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)

from functools import wraps


def type_logger(func):
    @wraps(func)
    def inner_func(*args, h=5):
        res = []
        for arg in args:
            res.append(f'{func.__name__}({arg}: {type(arg)})')
            print(func(arg), type(func(arg)))  # выводим тип значения функции
        res.append(f'{func.__name__}({h}: {type(h)})')  # работаем с именованным аргументом
        print(func(h), type(func(h)))  # выводим тип значения функции для именованного аргумента
        print(*res, sep=', ')  # выводим данные через запятую. Список - исключительно для того, чтобы в одну строку.
    return inner_func


@type_logger
def calc_cube(x):
    return x ** 3


calc_cube(5, 6, h=7)
