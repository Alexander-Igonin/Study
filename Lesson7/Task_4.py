'''
Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время года,
которому этот месяц принадлежит (зима, весна, лето или осень)
'''
def seasons(a):
    if a == 12 or a <= 2:
        return str('зима')
    elif a > 2 and a <= 5:
        return str('весна')
    elif a > 5 and a <= 8:
        return str('лето')
    elif a > 8 and a <= 11:
        return str('осень')
s = int(input('Введите число месяца: '))
print(seasons(s))