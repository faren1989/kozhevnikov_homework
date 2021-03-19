# 7. * (вместо 6) Добавить возможность редактирования данных при помощи отдельного скрипта: передаём ему номер
# записи и новое значение. При этом файл не должен читаться целиком — обязательное требование.
# Предусмотреть ситуацию, когда пользователь вводит номер записи, которой не существует.

import sys

change_sale = open('bakery.txt', 'r+', encoding='utf-8')

line = change_sale.readline()
line_length = len(line)
change_sale.seek(0)

lines_count = 0
for line in change_sale:
    if line.strip():
        lines_count += 1
change_sale.seek(0)

if int(sys.argv[1]) > lines_count:
    exit(print('Записи под таким номером не существует'))

change_sale.seek((int(sys.argv[1]) - 1) * (line_length + 1))
if ',' in sys.argv[2]:
    sale = sys.argv[2].split(',')
else:
    sale = (sys.argv[2] + ',00').split(',')
sale[0] = f'{int(sale[0]):04d}'
if len(sale[1]) == 1:
    sale[1] = str(int(sale[1]) * 10)
sale = ','.join(sale).replace(',', '.')
change_sale.write(sale)
change_sale.seek(0)

change_sale.close()