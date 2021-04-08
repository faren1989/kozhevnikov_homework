# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере.
# Запрашивать у пользователя данные и заполнять список необходимо только числами.
# Класс-исключение должен контролировать типы данных элементов списка

class ListError(Exception):
    def __init__(self, txt):
        self.txt = txt


result_list = []
while True:
    try:
        list_el = input('Введите число для добавления в список(для выхода введите "q"): ')
        if list_el == 'q':
            exit('Пока!')
        if not list_el.isdigit():
            raise ListError('Это не число!\n')
    except ListError as err:
        print(err)
    else:
        result_list.append(int(list_el))
        print(f'Список чисел: {result_list}\n')
