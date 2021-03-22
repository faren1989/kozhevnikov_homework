# Для чтения данных реализовать в командной строке следующую логику:
# . просто запуск скрипта — выводить все записи;
# . запуск скрипта с одним параметром-числом — выводить все записи с номера, равного этому числу, до конца;
# . запуск скрипта с двумя числами — выводить записи, начиная с номера, равного первому числу, по номер,
# равный второму числу, включительно.
# Подумать, как избежать чтения всего файла при реализации второго и третьего случаев.
# Данные хранить в файле bakery.csv в кодировке utf-8. Нумерация записей начинается с 1.
#
# Примеры запуска скриптов:
# python show_sales.py
# 5978,5
# 8914,3
# 7879,1
# 1573,7
# python show_sales.py 3
# 7879,1
# 1573,7
# python show_sales.py 1 3
# 5978,5
# 8914,3
# 7879,1

import sys

show_sales = open('bakery.txt', 'r', encoding='utf-8')
line = show_sales.readline()
line_length = len(line)
show_sales.seek(0)

if len(sys.argv[1:]) == 1:
    show_sales.seek((int(sys.argv[1]) - 1) * (line_length + 1))
    for line in show_sales:
        print(f'{float(line)}'.replace(".", ","))

elif len(sys.argv[1:]) == 2:
    show_sales.seek((int(sys.argv[1]) - 1) * (line_length + 1))
    idx = 0
    while idx <= (int(sys.argv[2]) - int(sys.argv[1])):
        for line in show_sales:
            print(f'{float(line)}'.replace(".", ","))
            idx += 1
            break

else:
    for line in show_sales:
        if line.strip():
            print(f'{float(line)}'.replace(".", ","))

show_sales.close()
