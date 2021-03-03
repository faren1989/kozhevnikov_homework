# 3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имен, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# Например:
# >>> >>> thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"], "П": ["Петр"]
# }
# Подумайте: полезен ли будет вам оператор распаковки? Сможете ли вы вернуть отсортированный по ключам словарь?


def thesaurus(*names):
    keys = []
    for name in names:
        if name[0] not in keys:
            keys.append(name[0])
    keys.sort()
    values = []
    idx = 0
    while idx < len(keys):
        value = []
        for name in names:
            if name[0] in keys[idx]:
                value.append(name)
        values.append(value)
        idx += 1
    print(dict(zip(keys, values)))


names = ["Иван", "Мария", "Петр", "Илья", "Борислав", "Григорий", "Ирина", "Михаил"]

thesaurus(*names)
