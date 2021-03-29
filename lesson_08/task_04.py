# 4. Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции
# и выбрасывать исключение ValueError, если что-то не так, например:
# def val_checker...
#     ...
#
#
# @val_checker(lambda x: x > 0)
# def calc_cube(x):
#    return x ** 3
#
#
# >>> a = calc_cube(5)
# 125
# >>> a = calc_cube(-5)
# Traceback (most recent call last):
#   ...
#     raise ValueError(msg)
# ValueError: wrong val -5
# Примечание: сможете ли вы замаскировать работу декоратора?

from functools import wraps


def val_checker(func):
    @wraps(func)
    def inner_func(*args, **kwargs):
        for arg in args:
            if type(arg) != int or type(arg) == float or arg < 0:
                raise ValueError('Неправильный формат числа. Число должно быть целым и больше ноля')
            elif arg > 0:
                result = func(arg)
                print(result)
    return inner_func


@val_checker
def calc_cube(x):
    return x ** 3


calc_cube(5)
