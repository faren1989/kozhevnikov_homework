# Задание 1. Функция-генератор rand_nums
# Написать функцию-генератор rand_nums, генерирующую N случайных целых чисел в диапазоне 1 до 100 (включительно).
# Количество чисел N, которое выдаст генератор передается в функцию через параметр:
#
# >>> rand15 = rand_nums(15)
# >>> next(rand15) # 1-й вызов
# 11
# >>> next(rand15) # 2-й вызов
# 38
# ...
# >>> next(rand15) # 15-й вызов
# 7
# >>> next(rand15) # 16-й вызов
# ...StopIteration...

import random


def rand_nums(limit):
    for i in range(limit):
        yield random.choice(range(1, 101))
        i += 1


# rand15 = rand_nums(15)
# print(next(rand15))
# print(next(rand15))
# print(next(rand15))
# print(next(rand15))
# print(next(rand15))
# print(next(rand15))
# print(next(rand15))
# print(next(rand15))
# print(next(rand15))
# print(next(rand15))
# print(next(rand15))
# print(next(rand15))
# print(next(rand15))
# print(next(rand15))
# print(next(rand15))
# print(next(rand15))
# print('=======')
#
# # вариант покороче, но здесь тогда не выполняется условие задачи в плане создания функции
# limit = 15
# num2 = (random.choice(range(1, 101)) for i in range(limit))
# print(next(num2))

