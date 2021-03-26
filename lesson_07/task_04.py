# 4. Написать скрипт, который выводит статистику для заданной папки в виде словаря,
# в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
# а значения — общее количество файлов (в том числе и в подпапках),
# размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
#     {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }
# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.

import os

result = {100: 0, 1000: 0, 10000: 0, 100000: 0}
for cdir, subdirs, files in os.walk('C:/Users/faren/Desktop/GeekBrains'):
    for file in files:
        if os.stat(os.path.join(cdir, file)).st_size < 100:
            result[100] += 1
        elif 100 <= os.stat(os.path.join(cdir, file)).st_size < 1000:
            result[1000] += 1
        elif 1000 <= os.stat(os.path.join(cdir, file)).st_size < 10000:
            result[10000] += 1
        elif 10000 <= os.stat(os.path.join(cdir, file)).st_size < 100000:
            result[10000] += 1
print(result)
