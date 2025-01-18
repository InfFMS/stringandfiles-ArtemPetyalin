# Откройте текстовый файл task2.txt для чтения.
# Считайте его содержимое в строку.
# Найдите и замените все вхождения слова "Python" на слово "Питон" (регистр учитывать).
# Запишите обновленный текст в новый файл с другим именем.
# Выведите на экран сообщение о количестве произведённых замен.
f = open('task2.txt', encoding='utf-8')
text_arr = f.read().split('\n')

for i in range(len(text_arr)):
    text_arr[i] = text_arr[i].split()
print(text_arr)

counter = 0
for i in range(len(text_arr)):

    for j in range(len(text_arr[i])):

        if text_arr[i][j] == 'python':
            text_arr[i].pop(j)
            text_arr[i].insert(j, 'питон')
            counter += 1

        elif text_arr[i][j] == 'Python':
            text_arr[i].pop(j)
            text_arr[i].insert(j, 'Питон')
            counter += 1

text_str = ''

for i in range(len(text_arr)):

    for j in range(len(text_arr[i])):

        if j == len(text_arr[i]) - 1:
            text_str = text_str + text_arr[i][j] + '\n'

        else:
            text_str = text_str + text_arr[i][j] + ' '

text_str = text_str[:-1]
f = open('new_file.txt', 'x', encoding='utf-8')
f.write(text_str)
f = open('new_file.txt', encoding='utf-8')
print(f.read())
print(counter)


