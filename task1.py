# Откройте текстовый файл для чтения task1.txt.
# Подсчитайте:
# Общее количество строк в файле.
# Общее количество слов во всем тексте файла.
# Общее количество символов (включая пробелы).
# Выведите полученную статистику на экран.
f = open("task1.txt", encoding = "utf-8")
text = f.read()
print('Quantity of lines:', len(text.split('\n')))
words = 1
newtext_arr = text.split('\n')
newtext = ''

for i in range(len(newtext_arr) - 1):
    newtext = newtext + newtext_arr[i].strip() + ' '

newtext = newtext + newtext_arr[-1]

for i in range(len(newtext)):

    if newtext[i] == ' ':
        words += 1

    elif newtext[i] == '-' and newtext[i - 1] == ' ':
        words -= 1

    elif newtext[i] == '.' or newtext[i] == '!' or newtext[i] == '?':
        words -= 1

    if i == len(newtext) - 1:
        words += 1

    if newtext[i] == '.' and newtext[i - 1] == '.' and (newtext[i - 2] == '.' or newtext[i - 2] == '?' or newtext[i - 2] == '!'):
        words += 2

print('Quantity of words:', words)
