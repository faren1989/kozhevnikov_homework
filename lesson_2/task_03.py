# Задание 3
# *(вместо задачи 2) Решить задачу 2 не создавая новый список (как говорят, in place). Эта задача намного серьёзнее,
# чем может сначала показаться.

text = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
idx = 0
while idx < len(text):
    for i in text:
        if i.isdigit() == True:
            text.remove(text[idx])
            text.insert(idx, f'"{int(i):02d}"')
            idx += 1
        elif i[1:].isdigit():
            text.remove(text[idx])
            text.insert(idx, f'"{int(i):+03d}"')
            idx += 1
        else:
            text.remove(text[idx])
            text.insert(idx, i)
            idx += 1
print(' '.join(text))
