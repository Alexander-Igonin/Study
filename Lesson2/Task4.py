"""
 Дано целое, положительное, трёхзначное число. Например: 123, 867, 374.
 Необходимо его перевернуть. Например, если ввели число 123, то должно получиться на выходе ЧИСЛО 321.
"""

a = input('Введите три числа: ')

a1 = a[2]
a2 = a[1]
a3 = a[0]
anw = a1 +a2 +a3

print(int(anw))

