'''
1. В текстовый файл построчно записаны имя и фамилия учащихся класса и их оценки
Вывести на экран всех учащихся, чей средний балл меньше 5, также посчитать и вывести
средний балл по классу. Так же,
 записать в новый файл всех учащихся в формате "Фамилия И. Ср. балл":
'''


lst = []
newLst = []
evr = []
uplLst = []

def createNewList():
    '''редактирует исходний файл и сохраняет в список newLst'''

    file = open('file.txt', 'r', encoding='UTF-8')
    lst = file.readlines()
    file.close()
    lst = list(map(lambda x: x.strip('\n'), lst))       #удаление \n

    for i in lst:       #создание списка
        newLst.append(i.split(' '))

    for x in range(len(newLst)):        #удаление пробелов
        n = 2
        while n > 0:
            for t in newLst[x]:
                if t == '':
                    newLst[x].remove(t)
            n -= 1


def lowestThanFive():
    '''
    выводит на экран учеников со средней оценкой меньше 5
    Также выводит на экран среднюю оценку всего класса
    '''

    for i in range(len(newLst)):
        n = 0
        k = 2
        for d in range(len(newLst)):
            n += int(newLst[i][int(k)])
            k += 1
        evr.append(n / 12)
        if n / 12 < 5:
            print(newLst[i])

    print()
    print('Средняя оценка класса: ', "%.1f" % (sum(evr) / 12))


def createUploadList():
    '''создает новый список для записи в файл'''

    z = 0
    for i in range(len(newLst)):
        uplLst.append(newLst[i][0:2])
        uplLst[i] = uplLst[i][0] + ' ' + uplLst[i][1][0] + '.' + ' '*6 + '%.1f' % evr[z]
        z += 1


def writeNewFile():
    '''создает новый текстовый файл на диске и записывает список учеников со средним баллом'''

    res = open('result.txt', 'w', encoding='UTF-8')
    for i in uplLst:
        res.write(str(i).rjust(21) + '\n')
    res.close()


createNewList()
lowestThanFive()
createUploadList()
writeNewFile()