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

my_project = {'settings': ['__init__.py', 'dev.py', 'prod.py'],
              'mainapp': ['__init__.py', 'models.py', 'views.py',
                  {'templates':
                              {'mainapp':
                                            ['base.html', 'index.html']}}],
              'authapp': ['__init__.py', 'models.py', 'views.py',
                  {'templates':
                              {'authapp':
                                            ['base.html', 'index.html']}}]}

if not os.path.exists('my_project'):
    os.mkdir('my_project')
for key in my_project.keys():
    if not os.path.exists(f'my_project/{key}'):
        os.mkdir(f'my_project/{key}')
    if type(my_project[key]) == list:
        for i in my_project[key]:
            if type(i) == str:
                f = open(f'./my_project/{key}/{i}', 'w', encoding='utf8')
                f.close()
            else:
                try:
                    for key2 in i.keys():
                        if not os.path.exists(f'my_project/{key}/{key2}'):
                            os.mkdir(f'my_project/{key}/{key2}')
                        if type(i[key2]) == list:
                            for j in i[key2]:
                                if type(j) == str:
                                    f = open(f'./my_project/{key}/{key2}/{j}', 'w', encoding='utf8')
                                    f.close()
                        else:
                            j = i[key2]
                            try:
                                for key3 in j.keys():
                                    if not os.path.exists(f'my_project/{key}/{key2}/{key3}'):
                                        os.mkdir(f'my_project/{key}/{key2}/{key3}')
                                    if type(j[key3]) == list:
                                        for n in j[key3]:
                                            if type(n) == str:
                                                f = open(f'./my_project/{key}/{key2}/{key3}/{n}', 'w', encoding='utf8')
                                                f.close()
                            except AttributeError:
                                continue
                except AttributeError:
                    continue

# Четсно говоря, мне стыдно за такое решение и здесь все легко сломается, если куда-нибудь что-нибудь добавить, но
# другого решения я не нашел=/