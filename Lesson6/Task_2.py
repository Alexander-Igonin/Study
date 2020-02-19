'''
Даны два списка чисел. Посчитайте, сколько чисел содержится одновременно как в первом списке, так и во втором.
'''
from random import randint

lst1 = set([randint(1, 10) for _ in range(15)])
lst2 = set([randint(1, 10) for _ in range(15)])
print(len(lst1) + len(lst2))


