# 1. Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает
# имя пользователя и почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден,
# выбросить исключение ValueError.
# Пример:
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru
# Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении;
# имеет ли смысл в данном случае использовать функцию re.compile()?

import re


def email_parse(email):
    login_name, mail = re.split(r'@', email)[0], re.split(r'@', email)[1]
    pattern = re.compile(r'([а-яА-Я`~@!#$%^&*()_№=+{};:<>,/?\'\"\[\]\\-])')
    validate_login = pattern.search(login_name)
    validate_mail = pattern.search(mail)
    if validate_login:
        symbol = validate_login.groups()[0]
        raise ValueError(f'"{symbol}" - недопустимый символ в адресе почты')
    elif validate_mail:
        symbol = validate_mail.groups()[0]
        raise ValueError(f'"{symbol}" - недопустимый символ в адресе почты')
    elif '.' not in mail:
        raise ValueError('Забыли указать домен')
    else:
        return {login_name: mail}


email = input('Введите адрес электронной почты: ')
parse_result = email_parse(email)
print(parse_result)
