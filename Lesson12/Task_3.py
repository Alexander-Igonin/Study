'''
Написать функцию, которая принимает в качестве параметра целое, многозначное число. Функция должна вернуть сумму произведения каждой цифры на её порядковый номер. Например:
	есть число 874658734
	8 именн порядковый номер 1,
	7 - 2
	4 - 3
	6 - 4
	5 - 5 и т. д.
	необходимо посчитать: 8 * 1 + 7 * 2 + 4 * 3 + 6 * 4 + 5 * 5 .....
	Задачу надо решить с использование list comprehension и функции sum() в ОДНУ строку.
'''

def intToList(num):
    result = []
    while num > 0:
        result.append(num % 10)
        num //= 10

    result.reverse()
    return result


def func(num):
    lst = intToList(num)

    return sum(list(map(lambda x, b: x * (b + 1), lst, [i for i in range(len(lst))])))

print(func(54843513))