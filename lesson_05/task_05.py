# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, например:
# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]
# Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

unique_numbers = set()
tmp_numbers = set()
for i in src:
    if i not in tmp_numbers:
        unique_numbers.add(i)
    else:
        unique_numbers.discard(i)
    tmp_numbers.add(i)


result = [j for j in src if j in unique_numbers]
print(result)
