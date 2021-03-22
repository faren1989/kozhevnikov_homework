# 2. * (вместо задачи 1) Доработать предыдущую функцию num_translate_adv():
# реализовать корректную работу с числительными, начинающимися с заглавной буквы. Например:
# >>> >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"

vocabulary = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


def num_translate_adv(word):
    if word.istitle() == True and word.lower() in vocabulary:
        word = word.lower()
        number = vocabulary.get(word)
        print(number.title())
    else:
        number = vocabulary.get(word)
        print(number)

word = input('Введите число. Для выхода нажмите "q":')
while word != 'q':
    translate = num_translate_adv(word)
    word = input('Введите число. Для выхода нажмите "q":')
