# Откройте текстовый файл task3.txt для чтения.
# Извлеките все уникальные слова из файла (слова разделяются пробелами и знаками пунктуации).
# Подсчитайте, сколько раз каждое уникальное слово встречается в тексте.
# Запишите результаты в новый файл в формате:
# слово1: количество
# слово2: количество
#
# Убедитесь, что слова записаны в алфавитном порядке.
import re
f = open('task3.txt', encoding='utf-8')
text = f.read().lower()
text = re.split(r'[ .,\n]+', text)
text.sort()
text2 = text
f.close()
unic_list = []

for i in range(len(text)):
    copies = 1
    for j in range(i, len(text)):

        if text[i] == text[j] and i != j:
            copies += 1

        elif text[i] == '':
            copies += 1

    if copies == 1:
        unic_list.append(text[i])

quantities = []

for i in range(len(unic_list)):
    counter = 0

    for j in range(len(text)):

        if unic_list[i] == text[j]:
            counter += 1

    quantities.append(counter)

f = open('task3answer.txt', 'x', encoding='utf-8')

for i in range(len(unic_list)):
    f.write(str(unic_list[i]) + ': ' + str(quantities[i]) + '\n')

