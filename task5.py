# Откройте текстовый файл task5.txt для чтения.
# Найдите самое длинное слово в тексте. Если таких слов несколько, выберите первое из них.
# Запишите это слово и его длину в новый файл в формате:
# Самое длинное слово: слово
# Его длина: длина
#
# Выведите это слово и длину в консоль.
import re
f = open('task5.txt', encoding='utf-8')
text = re.split(r'[.,!? \n]+', f.read())
text.pop(-1)
f.close()
maxlen = len(text[0])
index = 0

for i in range(len(text)):

    if len(text[i]) > maxlen:
         maxlen = len(text[i])
         index = i

print('The longest word: ', text[index])
print('Its length:', maxlen)