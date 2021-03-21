# 1. Не используя библиотеки для парсинга, распарсить (получить определённые данные)
# файл логов web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) —
# получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
#
# [
# ...
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('173.255.199.22', 'GET', '/downloads/product_2'),
# ...
# ]
#
# Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.

# import requests
#
# f = open('nginx_logs.txt', 'w', encoding='utf8')
# f.write(str(requests.get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs').\
#         content, encoding='utf8'))
# f.close

result = []
with open('nginx_logs.txt', 'r', encoding='utf8') as f:
    for line in f:
        line = line.split()
        result.append((line[0], line[5].strip('"'), line[6]))
        # я счел возможным поступить так, поскольку формат всех
        # строк одинаковый и мы точно знаем, где и что лежит.

# Вообще, можно было бы не создавать список, а сразу бежать по строкам логов и в новый файл добавлять данные.
# Но поскольку в условии задачи список составить надо, то он в решении тоже есть и бежим по нему.
with open('result.txt', 'w', encoding='utf8') as result_txt:
    for i in result:
        ip_addr, rqst_type, resource = i
        result_txt.write(f'{ip_addr} {rqst_type} {resource}\n')

# print(result)


