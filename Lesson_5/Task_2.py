rows = int(input('Высота фигуры: '))
cols = rows * 2

for i in range(rows):
    for a in range(cols):
        if i == 0 and a == cols // 2:
            print('* ', end='')
        elif i == rows - 1 and a > 0:
            print('* ', end='')
        elif a > cols // 2 - i and a < cols // 2 + i:
            print('* ', end='')
        elif a == cols // 2 - i or a == cols // 2 + i :
            print('* ', end='')
        else:
            print('  ', end='')
    print()