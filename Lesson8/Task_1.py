'''
Каждый кортеж состоит из номера заказа и произведения
цены на товары и количества. Стоимость товара должена быть увеличена на $10, если
стоимость заказа меньше $100. Программа должна использовать lambda и map.
'''

lst = [
[34587, 'Learning Python, Mark Lutz', 4, 40.95],
[98762, 'Programming Python, Mark Lutz', 5, 56.80],
[77226, 'Head First Python, Paul Barry', 3, 32.95],
[88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
]

x1 = (lst[0][2:4])
x2 = (lst[1][2:4])
x3 = (lst[2][2:4])
x4 = (lst[3][2:4])


xall = [x1, x2, x3, x4]
xall2 = []


xall2 = list(map(lambda a: a[0] * a[1], xall))
#print(xall2)

n = 0
for _ in xall2:
    if _ < 100:
       lst[n][3] = lst[n][3] + 10
    n += 1
#print(lst)

n = 0
for i in lst:
    del lst[n][1]
    n += 1
#print(lst)


n = 0
for n in range(4):
    x = lst[n].pop(2)
    lst[n][1] = lst[n][1] * x
#print(lst)


lst = tuple(lst[0]), tuple(lst[1]), tuple(lst[2]), tuple(lst[3])
print(lst)