def is_year_leap(a):
    if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
        return str('False')
    else:
        return str('True')

year = int(input('Введите год в виде YYYY '))
print(is_year_leap(year))