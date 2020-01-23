'''
2. Создать текстовый файл, записать в него построчно данные, которые вводит пользователь. Окончанием ввода пусть служит
пустая строка. Каждая введённая строка, в файле, должна начинаться с новой строки.
'''

file = open('result.txt', 'w', encoding='UTF-8')

while True:
    text = input('Enter text. For exit enter one SPACE. ') #выход из программы 1 пробел
    if text == ' ':
        break
    else:
        file.write(text + '\n')

file.close()
