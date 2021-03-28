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
    login_name, mail = re.search(r'(.+@)(.+)', email).groups()
    validate_login = re.search(r'([а-яА-Я`~@!#$%^&*()_№=+{};:<>,./\?\'\"\[\]\\-])', login_name[:-1])
    validate_mail = re.search(r'([а-яА-Я`~@!#$%^&*()_№=+{};:<>,/\?\'\"\[\]\\-])', mail)
    if validate_login:
        symbol = validate_login.groups()[0]
        raise ValueError(f'"{symbol}" - недопустимый символ в адресе почты')
    elif validate_mail:
        symbol = validate_mail.groups()[0]
        raise ValueError(f'"{symbol}" - недопустимый символ в адресе почты')
    elif '.' not in mail:
        raise ValueError('Забыли указать домен')
    else:
        return {login_name[:-1]: mail}


email = input('Введите адрес электронной почты: ')
parse_result = email_parse(email)
print(parse_result)
