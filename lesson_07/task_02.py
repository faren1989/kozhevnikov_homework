# 2. * (вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
# |--my_project
#    |--settings
#    |  |--__init__.py
#    |  |--dev.py
#    |  |--prod.py
#    |--mainapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--mainapp
#    |        |--base.html
#    |        |--index.html
#    |--authapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--authapp
#    |        |--base.html
#    |        |--index.html
# Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом текстовом редакторе «руками»
# (не программно);
# предусмотреть возможные исключительные ситуации, библиотеки использовать нельзя.

import os

src = open('configure.txt', 'r', encoding='utf8')

for line in src:
    cdir = line.strip().split('=')[0]
    content = line.strip().split('=')[1].split(',')
    if not os.path.exists(cdir):
        os.mkdir(cdir)
    for i in content:
        if '.' in i:
            file = open(f'{cdir}/{i}', 'w', encoding='utf8')
            file.close()



src.close()