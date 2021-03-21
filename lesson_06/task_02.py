# 2. * (вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего
# задания.
# Примечания: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами,
# размер которых превышает объем ОЗУ компьютера.

import time
from sys import getsizeof

# ВАРИАНТ 1
start1 = time.perf_counter()
# Сделаем список, в котором у нас будут храниться все адреса, с которых поступали запросы
all_addresses = []

# Сделаем множество, где будут храниться уникальные адреса, с которых поступали запросы
unique_addresses = set()

# Заполним список и множество
with open('nginx_logs.txt', 'r', encoding='utf8') as f:
    for line in f:
        line = line.split()
        all_addresses.append(line[0])
        unique_addresses.add(line[0])

# Пробежимся по множеству, и выясним, с какого адреса чаще всего поступали запросы
spamer_count = 0
spamer_ip = None
for i in unique_addresses:
    if all_addresses.count(i) > spamer_count:
        spamer_count = all_addresses.count(i)
        spamer_ip = i

end1 = time.perf_counter()
td = end1 - start1
print(spamer_count, spamer_ip, f'{td:.06f}', getsizeof(all_addresses), getsizeof(unique_addresses))

# ВАРИАНТ 2
start2 = time.perf_counter()
# Сделаем словарь и заполним его, ключи - адреса, значения - количество вызовов
addresses_and_counts = {}
with open('nginx_logs.txt', 'r', encoding='utf8') as f:
    for line in f:
        line = line.split()
        addresses_and_counts.setdefault(line[0], 0)
        addresses_and_counts[line[0]] += 1
spamer_count = 0
spamer_ip = None
for i in addresses_and_counts.keys():
    if addresses_and_counts[i] > spamer_count:
        spamer_count = addresses_and_counts[i]
        spamer_ip = i
end2 = time.perf_counter()
td2 = end2 - start2
print(spamer_count, spamer_ip, f'{td2:.06f}', getsizeof(addresses_and_counts))

# Очевидно, что словарь рулит.
