# Задание 5. * Вызов с командной строки
# Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли,
# а коды валют ему дожны передавать через аргументы командной строки (там может быть один или несколько кодов).
# Вывод курсов сделать в том же порядке, что присланные аргументы
# Например:
#
# python task5.py USD EUR
# USD 75.18, 2020-09-05
# EUR 80.35, 2020-09-05

import sys
from utils import get_currency_rate
result = get_currency_rate(*sys.argv[1:])  # индекс [1:], чтобы название файла не попадало в аргументы
for key in result:
    if result[key] is None:
        print(result[key])
    else:
        currency_nominal, currency_value, date = result[key]
        print(f'{currency_nominal} {key} = {currency_value:.02f}, {date}')
