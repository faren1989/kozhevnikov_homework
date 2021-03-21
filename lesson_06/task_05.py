# 5. ** (вместо 4) Решить задачу 4 и реализовать интерфейс командной строки, чтобы можно было задать путь
# к обоим исходным файлам и путь к выходному файлу со словарём. Проверить работу скрипта для случая,
# когда все файлы находятся в разных папках.

import sys
import json

if len(sys.argv[1:]) < 3:
    print('Вы не задали путь к одному из файлов')

users = open(sys.argv[1], 'r', encoding='utf8')
hobby = open(sys.argv[2], 'r', encoding='utf8')

life_style = {}

users_length = 0
for line in users:
    if line.strip():
        users_length += 1

hobby_length = 0
for line in hobby:
    if line.strip():
        hobby_length += 1

if hobby_length > users_length:
    exit(1)

users.seek(0)
hobby.seek(0)

for line in users:
    surname, name, fathers_name = line.strip().split(',')
    if line.strip():
        user = (surname, name, fathers_name)
        life_style.setdefault(user, None)
    for line in hobby:
        his_hobby = line.strip().split(',')
        if line.strip():
            life_style[user] = his_hobby
        break

users.close()
hobby.close()

print(life_style)

with open(sys.argv[3], 'w', encoding='utf8') as dict_file:
    life_style_new = json.dumps(life_style, ensure_ascii=False)
    dict_file.write(life_style_new)

with open(sys.argv[3], 'r', encoding='utf8') as dict_file:
    src = dict_file.read()
    result = json.loads(src)
    print(result, '\n', type(result))
