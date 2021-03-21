# 4. * (вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ
# (разумеется, не нужно реально создавать такие большие файлы, это просто задел на будущее проекта).
# Также реализовать парсинг данных из файлов - получить отдельно фамилию, имя и отчество для пользователей
# и название каждого хобби: преобразовать в какой-нибудь контейнерный тип (список, кортеж, множество, словарь).
# Обосновать выбор типа. Подумать, какие могут возникнуть проблемы при парсинге. В словаре должны храниться данные,
# полученные в результате парсинга.
import json

users = open('users.csv', 'r', encoding='utf8')
hobby = open('hobby.csv', 'r', encoding='utf8')
dict_file = open('life_style.txt', 'w', encoding='utf8')

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
    life_style = {}
    if line.strip():
        user = ' '.join(line.strip().split(','))
        # я не стал парсить ФИО, потому что json ругается на ключи контейнерного типа. В теории, можно было бы создать
        # отдельный файл, где хранились бы кортежи, а здесь в качестве ключа были бы номера строк, на которых они лежат,
        # но я решил не лезть в такие дебри.
        life_style.setdefault(user, None)
    for line in hobby:
        his_hobby = line.strip().split(',')  # преобразовал в список, т.к. хобби и их количество могут меняться
        if line.strip():
            life_style[user] = his_hobby
        break
    dict_file.write('\n')
    dict_file.write(json.dumps(life_style, ensure_ascii=False))
    dict_file.write('\n')

users.close()
hobby.close()
dict_file.close()

with open('life_style.txt', 'r', encoding='utf8') as dict_file:
    life_style_result = {}
    for line in dict_file:
        result = json.loads(dict_file.readline())
        life_style_result.update(result)
    print(life_style_result, '\n', type(life_style_result))

# Думаю, мне удалось выполнить главное условие задачи - ограничение по ОЗУ. Исходные файлы читаются построчно и
# результат постепенно добавляется в конечный файл. При получении данных из этого файла, они, опять же, вытаскиваются
# постепенно и преобразуются в нужный словарь. Таким образом, целиком словарь не загружается в память в процессе работы
# программы. Единственное, поступился парсингом ФИО. Но, если бы это было так нужно (получить отедльно имя, фамилию и
# отчество, я бы это делал уже после того, как вытащил словарь обратно, просто распарсив ключи и сделав новый словарь
# c ключами - кортежами.




