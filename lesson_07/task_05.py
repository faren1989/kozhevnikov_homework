# 5. * (вместо 4) Написать скрипт, который выводит статистику для заданной папки в виде словаря,
# в котором ключи те же, а значения — кортежи вида (<files_quantity>, [<files_extensions_list>]), например:
#   {
#       100: (15, ['txt']),
#       1000: (3, ['py', 'txt']),
#       10000: (7, ['html', 'css']),
#       100000: (2, ['png', 'jpg'])
#     }
# Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили скрипт.

# # os.path.basename(file))

import os

result = {}
idx1 = 0
file_types1 = set()
idx2 = 0
file_types2 = set()
idx3 = 0
file_types3 = set()
idx4 = 0
file_types4 = set()

for cdir, subdirs, files in os.walk('C:/Users/faren/Desktop/GeekBrains'):
    for file in files:
        if os.stat(os.path.join(cdir, file)).st_size < 100:
            idx1 += 1
            try:
                file_type = os.path.basename(file).split('.')
                file_types1.add(file_type[1])
            except IndexError:
                pass
        elif 100 <= os.stat(os.path.join(cdir, file)).st_size < 1000:
            idx2 += 1
            try:
                file_type = os.path.basename(file).split('.')
                file_types2.add(file_type[1])
            except IndexError:
                pass
        elif 1000 <= os.stat(os.path.join(cdir, file)).st_size < 10000:
            idx3 += 1
            try:
                file_type = os.path.basename(file).split('.')
                file_types3.add(file_type[1])
            except IndexError:
                pass
        elif 10000 <= os.stat(os.path.join(cdir, file)).st_size < 100000:
            idx4 += 1
            try:
                file_type = os.path.basename(file).split('.')
                file_types4.add(file_type[1])
            except IndexError:
                pass
result.setdefault(100, (idx1, list(file_types1)))
result.setdefault(1000, (idx2, list(file_types2)))
result.setdefault(10000, (idx3, list(file_types3)))
result.setdefault(100000, (idx4, list(file_types4)))
for k, v in result.items():
    print(f'{k}: {v}')
