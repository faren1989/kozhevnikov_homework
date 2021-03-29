# 2. * (вместо 1) Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
# для получения информации вида: (<remote_addr>, <request_datetime>, <request_type>, <requested_resource>,
# <response_code>, <response_size>), например:
#
# raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-"
# "Debian APT-HTTP/1.3 (0.9.7.9)"'
# parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')
# Примечание: вы ограничились одной строкой или проверили на всех записях лога в файле?
# Были ли особенные строки? Можно ли для них уточнить регулярное выражение?

import re


# ВАРИАНТ 1
def log_parse(line):
    try:
        remote_addr = re.search(r'(\d+\.\d+\.\d+\.\d+)', line)
        # print(remote_addr.groups()[0])
        a = remote_addr.groups()[0]
    except AttributeError:
        remote_addr = re.search(r'([:\d\w]+)', line)
        # print(remote_addr.groups()[0])
        a = remote_addr.groups()[0]

    date_and_time = re.search(r'(\[.+])', line)
    # print(date_and_time.groups()[0].strip('[').strip(']'))
    b = date_and_time.groups()[0].strip('[').strip(']')

    rqst_type = re.search(r'("[A-Z]+)', line)
    # print(rqst_type.groups()[0].strip('"'))
    c = rqst_type.groups()[0].strip('"')

    rqstd_resource = re.search(r'(/\w+/\w+_\d)', line)
    # print(rqstd_resource.groups()[0])
    d = rqstd_resource.groups()[0]

    code_and_size = re.search(r'" (\d+) (\d+) "', line)
    # print(code_and_size.groups())
    e = code_and_size.groups()[0]
    g = code_and_size.groups()[1]

    res = (a, b, c, d, e, g)
    return res


# ВАРИАНТ 2
# def log_parse(line):
#     res = re.split(r' ', line)
#     return (res[0], (f"{res[3].strip('[')} {res[4].strip(']')}"), res[5].strip('"'), res[6], res[8], res[9])


with open('nginx_logs.txt', 'r', encoding='utf8') as f:
    for line in f:
        parsed_line = log_parse(line)
        print(parsed_line)
