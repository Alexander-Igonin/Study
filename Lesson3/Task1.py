'''
. По данному целому числу N распечатайте все квадраты натуральных чисел, не превосходящие N, в порядке возрастания.
'''
a = int(input('Введите число: '))
i = 1
while i**2 <= a:
    print(i**2)
    i += 1