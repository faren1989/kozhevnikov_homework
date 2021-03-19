# 4. * (вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ
# (разумеется, не нужно реально создавать такие большие файлы, это просто задел на будущее проекта).
# Также реализовать парсинг данных из файлов - получить отдельно фамилию, имя и отчество для пользователей
# и название каждого хобби: преобразовать в какой-нибудь контейнерный тип (список, кортеж, множество, словарь).
# Обосновать выбор типа. Подумать, какие могут возникнуть проблемы при парсинге. В словаре должны храниться данные,
# полученные в результате парсинга.

users = open('users.csv', 'r', encoding='utf8')
hobby = open('hobby.csv', 'r', encoding='utf8')

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
        user = (surname, name, fathers_name)  # преобразовал в кортеж, т.к. имя у человека меняться вряд ли будет
        life_style.setdefault(user, None)
    for line in hobby:
        his_hobby = line.strip().split(',')  # преобразовал в список, т.к. хобби и их количество могут меняться
        if line.strip():
            life_style[user] = his_hobby
        break

users.close()
hobby.close()

print(life_style)
