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
print(text)
text2 = text
f.close()

unic_list = []
i = 0

while i < len(text) - 1:

    if text[i] == '':
        text.pop(i)

    else:
        j = i + 1

        while j < len(text):

            if text[i] == text[j]:
                text.pop(j)

            j += 1

    i += 1

amounts = []

for i in range(len(text)):
    counter = 0

    for j in range(len(text2)):

        if text[i] == text2[j]:
            counter += 1

    amounts.append(counter)

answer = []

f = open('task3answer.txt', 'x', encoding='utf-8')

for i in range(len(amounts)):
    stringichek = text[i] + ' - ' + str(amounts[i]) +  ' \n'
    f.write(stringichek)

f.read()
f.close()