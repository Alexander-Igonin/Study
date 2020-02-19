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

lst_n = list(map(lambda x: (x[0], round(x[2] * x[3] if x[2] * x[3] > 100 else x[2] * (x[3] + 10))), lst))
print(lst_n)