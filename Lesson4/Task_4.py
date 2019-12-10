'''
 Дана строка. Замените в этой строке все появления буквы `h` на букву `H`, кроме первого и последнего вхождения.
'''

#word = input('Введите текст: ')
word = 'hello huh how hi heria hp' #если испольовать input, закоментить эту строку
first = word.find('h')
first += 1
last = word.rfind('h')
last -= 1
a1 = word[:first]
a2 = word[last::]
a3 = word[first:last].replace('h', 'H')
result = a1 + a3 + a2
print(result)
