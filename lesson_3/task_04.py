# 4. * (вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки
# в формате «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий,
# а значения — словари, реализованные по схеме предыдущего задания и содержащие записи,
# в которых фамилия начинается с соответствующей буквы. Например:
# >>> >>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
# {
#     "А": {
#         "П": ["Петр Алексеев"]
#     },
#     "С": {
#         "И": ["Иван Сергеев", "Инна Серова"],
#         "А": ["Анна Савельева"]
#     }
# }
# Сможете ли вы вернуть отсортированный по ключам словарь?

# # функция, которая возвращает словарь, где ключи это первые буквы имен, а значения - имена и фамилии.
# def thesaurus(*names):
#     keys = []
#     for name in names:
#         if name[0] not in keys:
#             keys.append(name[0])
#     keys.sort()
#
#     values = []
#     idx = 0
#     while idx < len(keys):
#         value = []
#         for name in names:
#             if name[0] in keys[idx]:
#                 value.append(name)
#         values.append(value)
#         idx += 1
#     return dict(zip(keys, values))
#
#
# # функция, которая возвращает словарь, где ключи - первые буквы фамилий, а значения - словари из первой функции
# def thesaurus_adv(*names):
#
#     keys_surnames = []
#     for name in names:
#         surnames = name.split()[-1]
#         if surnames[0] not in keys_surnames:
#             keys_surnames.append(surnames[0])
#     keys_surnames.sort()
#
#     values_surnames = []
#     idx = 0
#     while idx < len(keys_surnames):
#         value = []
#         for name in names:
#             surnames = name.split()[-1]
#             if surnames[0] in keys_surnames[idx]:
#                 value.append(name)
#         values_surnames.append(value)
#         idx += 1
#
# # создаем вспомогательный список словарей, где ключи - первые буквы имени, а значения - имена и фамилии.
#     secondary_dictionary = []
#     for value in values_surnames:
#         small_dict = thesaurus(*value)
#         secondary_dictionary.append(small_dict)
#
#     return dict(zip(keys_surnames, secondary_dictionary))


def thesaurus_adv(*args):
    dictionary = {}
    for full_name in args:
        name, surname = full_name.split()
        first_letter_name = name[0]
        first_letter_surname = surname[0]
        dictionary.setdefault(first_letter_surname, {}).setdefault(first_letter_name, []).append(full_name)
    return dictionary

# исходный список имен и фамилий
names = [
    "Иван Сергеев", "Инна Серова", "Анна Савельева", "Петр Алексеев", "Илья Бондарев", "Борислав Янцев",
    "Григорий Явлинский", "Ирина Хакамада", "Михаил Горбачев"
]

main_dictionary = thesaurus_adv(*names)
for first_letter_surname in sorted(main_dictionary.keys()):
    print(f'{first_letter_surname}')
    for first_letter_name in sorted(main_dictionary[first_letter_surname].keys()):
        print(f' {first_letter_name}:{main_dictionary[first_letter_surname][first_letter_name]}')

