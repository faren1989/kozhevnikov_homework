# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class ZeroError(Exception):
    def __init__(self, txt):
        self.txt = txt


user_param1 = int(input('Введите делимое: '))
user_param2 = int(input('Введите делитель: '))

try:
    if user_param2 == 0:
        raise ZeroError('На ноль делить нельзя!')
except ZeroError as err:
    print(err)
else:
    result = user_param1 / user_param2
    print(f'Результат деления равен {result:.02f}')
