'''
Написать функцию для перевода десятичного числа в другую систему исчисления (2-36)
'''

from string import ascii_uppercase


def func(a, b):
    res = ''
    while a > 0:
        z = a % b
        if z >= 10:
            z = ascii_uppercase[z % 10]
        res += str(z)
        a //= b
    return res[::-1]

print(func(int(input('Введите число ')),int(input('Введите систему счисления 2-32 '))))