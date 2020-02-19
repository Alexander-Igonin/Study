'''
Написать функцию сортировки двухмерного списка МхМ (матрицы)
Значение М - задаётся пользователем, с клавиатуры. Может быть любым
целым, положительным числом, больше 5.
'''

from random import randint

rng = int(input('Размер матрицы, число больше 5: '))
if rng < 5:
    while rng < 5:
        rng = int(input('Введите число больше 5 !!!: '))

lst = [[randint(0, 50) for i in range(rng)] for i in range(rng)]
lst_sum = []

def calculate(lst):
    for i in range(len(lst)):
        sum = 0
        for _ in range(len(lst)):
            sum += lst[_][i]
        lst_sum.append(sum)

    for j in range(len(lst)):
        for x in range(len(lst) - 1):
            for y in range(len(lst) - 1 - x):
                if j % 2 == 0:
                    if lst[y][j] > lst[y + 1][j]:
                        lst[y][j], lst[y + 1][j] = lst[y + 1][j], lst[y][j]
                else:
                    if lst[y][j] < lst[y + 1][j]:
                        lst[y][j], lst[y + 1][j] = lst[y + 1][j], lst[y][j]


def matrixPrint(lst):
    for i in range(len(lst)):
        for _ in range(len(lst) - 1):
            print("%5d" % (lst[i][_]), end=' ')
        print()


calculate(lst)
lst.append(lst_sum)
matrixPrint(lst)