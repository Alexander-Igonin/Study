a = 'AABABBAABBBAB'


def func(str):
    c = ''
    for i in range(len(str)):
        if str[i] == 'A':
            c += 'B'
        elif str[i] == 'B':
            c += 'A'
    return c

print(a)
print(func(a))