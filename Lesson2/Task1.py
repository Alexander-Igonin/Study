"""
 n школьников делят k яблок поровну, неделящийся остаток остается в корзинке.
 Сколько яблок достанется каждому школьнику?
 Сколько яблок останется в корзинке?
 Программа получает на вход числа n и k и должна вывести искомое количество яблок (два числа).
"""


print('Программа покажет сколько школьнников разделили между собой заданное кол-во яблок поровну, а сколько осталось в корзине')
a = int(input('Введите число школьников: '))
b = int(input('Введите число яблок: '))
print('Каждому школьнику досталось ',b // a,' яблок')
print('В корзине осталось ',b % a,' яблок')