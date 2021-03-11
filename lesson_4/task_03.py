# Доработать функцию get_currency_rate(): теперь она должна возвращать курс и дату,
# на которую этот курс действует (взять из того же файла ЦБ РФ).
# Для значения курса используйте тип Decimal (https://docs.python.org/3.8/library/decimal.html) вместо float.
# Дата должна быть типа datetime.date.

import requests
from decimal import Decimal
import datetime
info = str(requests.get('http://www.cbr.ru/scripts/XML_daily.asp').content)


def get_currency_rate(*currency_names):
    currency_dict = {}
    for currency_name in currency_names:
        currency_name = currency_name.upper()
        if currency_name in info:
            # находим нужную валюту в строке и узнаем ее индекс
            currency_name_idx = info.index(currency_name)
            # находим значение этой валюты и узнаем индекс
            value_start_idx = info[currency_name_idx:].index('<Value>')
            value_end_idx = info[currency_name_idx:].index('</Value>')
            # по полученным индексам "вырезаем" значение валюты из строки и делаем нужный тип переменной
            value = info[currency_name_idx + value_start_idx + len('<Value>'):\
                         currency_name_idx + value_end_idx].split(',')
            value = Decimal('.'.join(value))
            # я решил вытащить еще и номанал, потому что некоторые валюты берутся в эквиваленте 100 или 10, например.
            # в таком случае вывод казахского тенге был бы некорректным
            nominal_start_idx = info[currency_name_idx:].index('<Nominal>')
            nominal_end_idx = info[currency_name_idx:].index('</Nominal>')
            nominal = info[currency_name_idx + nominal_start_idx + len('<Nominal>'):\
                           (currency_name_idx + nominal_end_idx)]
            # находим дату и переводим ее в нужный формат
            date = info[info.find('Date') + len('Date="'):info.find('Date') + len('Date="00/00/0000')].split('.')
            dd, mm, yyyy = int(date[0]), int(date[1]), int(date[2])
            date = datetime.date(yyyy, mm, dd)
            # записываем в словарь валюту и ее значения
            currency_dict[currency_name] = [nominal, value, date]
        else:
            currency_dict[currency_name] = None
    return currency_dict


currency_names = input('Введите через пробел код или коды валют, курс которых вас интересует:').split()
result = get_currency_rate(*currency_names)
for key in result:
    if result[key] is None:
        print(result[key])
    else:
        currency_nominal, currency_value, date = result[key]
        print(f'{currency_nominal} {key} = {currency_value:.02f}, {date}')


# Вообще, если бы мне в работе поставили задачу, чтобы функция возвращала текущую дату (дату на момент вызова функции),
# я бы пользовался datetime.date.today(), но поскольку по условию задачи нужно было вытащить дату именно с сайта, то я
# придумал решение, написанное выше.
