'''
Дан список чисел. Определите, сколько в нем встречается различных чисел.
'''

from random import randint

lst = set([randint(1, 10) for _ in range(20)])

print(lst)
print('Уникальных зачений в списке: ', len(lst))