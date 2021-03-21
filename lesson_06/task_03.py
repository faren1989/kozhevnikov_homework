# 3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
# Известно, что при хранении данных используется принцип: одна строка — один пользователь,
# разделитель между значениями — запятая. Написать код, загружающий данные из обоих файлов
# и формирующий из них словарь: ключи — ФИО, значения — данные о хобби.
#
# Сохранить словарь в файл. Проверить сохранённые данные.
#
# Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре значение None.
#
# Если наоборот — выходим из скрипта с кодом «1».
#
# При решении задачи считать, что объём данных в файлах во много
# раз меньше объема ОЗУ.

# Фрагмент файла с данными о пользователях (users.csv):
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
# Фрагмент файла с данными о хобби (hobby.csv):
# скалолазание,охота
# горные лыжи

import json

users = open('users.csv', 'r', encoding='utf8')
hobby = open('hobby.csv', 'r', encoding='utf8')

users_length = 0
hobby_length = 0

for line in users:
    if line.strip():
        users_length += 1
for line in hobby:
    if line.strip():
        hobby_length += 1

users.seek(0)
hobby.seek(0)

if hobby_length > users_length:
    exit(1)

life_style = {}

for line in users:
    user = ' '.join(line.strip().split(','))
    life_style.setdefault(user, None)
    for line in hobby:
        his_hobby = line.strip().replace(',', ', ')
        life_style[user] = his_hobby
        break

users.close()
hobby.close()

# Теперь разберемся с сохранением и чтением файла
with open('dict.txt', 'w', encoding='utf8') as dict_file:
    dict_file.write(str(life_style))

with open('dict.txt', 'r', encoding='utf8') as dict_file:
    result = dict_file.read()
    print(result, '\n', type(result))

# Чтобы не терялся тип данных, воспользуемся json
with open('dict.txt', 'w', encoding='utf8') as dict_file:
    dict_file.write(json.dumps(life_style, ensure_ascii=False))

with open('dict.txt', 'r', encoding='utf8') as dict_file:
    result = json.loads(dict_file.read())
    print(result, '\n', type(result))
