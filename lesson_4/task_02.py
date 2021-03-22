# Написать функцию get_currency_rate(), принимающую в качестве аргумента код валюты
# (например, USD, EUR, GBP, ...) в виде строки и возвращающую курс этой валюты по отношению к рублю.
# Код валюты может быть в произвольном регистре.
# Функция должна возвращать результат числового типа, например float.
# Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
# Используйте библиотеку requests, чтобы забрать актуальные данные из ЦБ РФ по адресу
# http://www.cbr.ru/scripts/XML_daily.asp.
#
# Выведите на экран курсы для доллара и евро, используя написанную функцию.
#
# Рекомендация: выполнить предварительно запрос к этой странице в обычном браузере, посмотреть содержимое ответа.

import requests
# я вытащил контент вне тела функции, чтобы не приходилось делать реквест при каждом вызове функции
info = str(requests.get('http://www.cbr.ru/scripts/XML_daily.asp').content)


def get_currency_rate(currency_name):
    if currency_name in info:
        # находим нужную валюту в строке и узнаем ее индекс
        currency_name_idx = info.index(currency_name)
        # находим значение этой валюты и узнаем индекс
        value_start_idx = info[currency_name_idx:].index('<Value>')
        value_end_idx = info[currency_name_idx:].index('</Value>')
        # по полученным индексам "вырезаем" значение валюты из строки и делаем нужный тип переменной
        value = info[currency_name_idx + value_start_idx + len('<Value>'):currency_name_idx + value_end_idx].split(',')
        value = float('.'.join(value))
        # я решил вытащить еще и номанал, потому что некоторые валюты берутся в эквиваленте 100 или 10, например.
        # в таком случае вывод казахского тенге был бы некорректным
        nominal_start_idx = info[currency_name_idx:].index('<Nominal>')
        nominal_end_idx = info[currency_name_idx:].index('</Nominal>')
        nominal = info[currency_name_idx + nominal_start_idx + len('<Nominal>'):(currency_name_idx + nominal_end_idx)]
        return [nominal, value]
    else:
        return None


currency_name = input('Введите код валюты, курс которой вас интересует:').upper()
result = get_currency_rate(currency_name)
if result is None:
    print(result)
else:
    currency_nominal, currency_value = result
    print(f'{currency_nominal} {currency_name} = {currency_value:.04f}')
