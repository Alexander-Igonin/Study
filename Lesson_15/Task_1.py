'''
1. Реализовать класс цифрового счетчика.
Обеспечьте возможность установки максимального и минимального значений,
увеличения счетчика на 1,
возвращения текущего значения.
'''


class Counter:

    def __init__(self, minimum, maximum):
        '''создание счетчика и установка минимального и максимального значения'''

        self.minimum = minimum
        self.maximum = maximum
        self.lst = [i for i in range(self.minimum, self.maximum + 1)]


    def nextSymbol(self):
        '''увеличние счетчика на 1 и возвращение текущего значения'''

        try:
            res = self.lst.pop(0)
        except IndexError:
            er = 'already maximum'
            return er
        return res

n = 0
g = Counter(10, 14)
print(g.nextSymbol())
print(g.nextSymbol())
print(g.nextSymbol())
print(g.nextSymbol())
print(g.nextSymbol())
print(g.nextSymbol())
print(g.nextSymbol())