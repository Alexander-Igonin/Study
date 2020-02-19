rows = int(input('Высота фигуры: ')) // 2 + 1
cols = rows * 2

for i in range(rows):
    for a in range(cols):
        if i == 0 and a == cols // 2:
            print('* ', end='')
        elif i == rows - 1 and a > 0:
            print('* ', end='')
        elif a > cols // 2 - i and a < cols // 2 + i:
            print('* ', end='')
        elif a == cols // 2 - i or a == cols // 2 + i:
            print('* ', end='')
        else:
            print('  ', end='')
    print()

for i in range(rows):

    for a in range(cols):
        if i == rows - 2 and a == cols // 2:
            print('* ', end='')
        elif a == i + 2 and a < rows:
            print('* ', end='')
        elif a == cols - (i + 2) and a > rows:
            print('* ', end='')
        else:
            print('  ', end='')

    print()