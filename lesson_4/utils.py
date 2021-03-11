import requests
from decimal import Decimal
import datetime
# я вытащил контент вне тела функции, чтобы не приходилось делать реквест при каждом вызове функции
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
