'''
аписать функцию `XOR_cipher`, принимающая 2 аргумента: строку, которую нужно зашифровать, и ключ шифрования, которая
возвращает строку, зашифрованную путем применения операции XOR (битовое исключающее ИЛИ) над символами строки с ключом.
Написать также функцию `XOR_uncipher`, которая по зашифрованной строке и ключу восстанавливает исходную строку.

'''


def XOR_cipher(string, key='p'):
    res = ''
    for i in range(len(string)):
        h = ord(string[i]) ^ ord(key)
        res += chr(h)
    return res
cipped = XOR_cipher('my name is Alexander Igonin')
print(cipped)

uncipped = XOR_cipher(cipped)  # зашифрованную строку расшифровываю той же функцией
print(uncipped)