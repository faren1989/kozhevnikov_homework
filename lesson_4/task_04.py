# Написать свой модуль utils и перенести в него функцию get_currency_rate()
# из предыдущего задания (второго или третьего).
# Создать скрипт (task4.py), в котором импортировать этот модуль и выполнить вызовы
# функции get_currency_rate() для доллара и евро. Результат вывести на экран в виде:
#
# если используется функция из 2-го задания:
# USD 75.18
# EUR 80.35
# либо, если используется функция из 3-го задания
# USD 75.18, 2020-09-05
# EUR 80.35, 2020-09-05

from utils import get_currency_rate

currency_name = input('Введите через пробел код или коды валют, курс которых вас интересует:').split()
result = get_currency_rate(*currency_name)
for key in result:
    if result[key] is None:
        print(result[key])
    else:
        currency_nominal, currency_value, date = result[key]
        print(f'{currency_nominal} {key} = {currency_value:.02f}, {date}')
