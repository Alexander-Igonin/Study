'''
2. Создать класс, описывающий группу студентов - `Group`. Данный класс хранит студентов в виде списка объектов `Student` также реализованного в виде соответствующего класса.
В классах реализовать необходимай набор атрибутов (Например класс `Student` должен иметь атрибуты `name`, `age`, `grades`), а так же необходимый набор методов экземпляра для работы с этими экземплярами.
'''


class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def getStudent(self):
        '''создает студента'''
        student = {'Name': self.name, 'Age': self.age, 'Grades': self.grades}

        return student


class Group:
    '''хранит список студентов'''

    group = []

    def addStudent(self, student):
        '''добавляет студента в общий список'''
        self.group.append(student)
        print('Студент', student['Name'],  'добавлен(а) в список')

    def deleteStudent(self, student):
        '''удаляет студента из общего списка'''
        try:
            i = self.group.index(student)
        except ValueError:
            print('Такого студента нет')
        else:
            del self.group[i]
            print('Студент', student['Name'],  'удален(а) из списка')

    def showGroup(self):
        '''выводит на экран список студентов'''
        print(self.group)


alex = Student('Alex', 27, [4, 6, 3, 7, 9])
lisa = Student('Lisa', 24, [3, 4, 6, 2, 3])
lena = Student('Lena', 30, [5, 3, 1, 7, 4])
maks = Student('Maks', 24, [5, 3, 7, 4, 7])

add = Group()
add.addStudent(alex.getStudent())
add.addStudent(lisa.getStudent())
add.addStudent(lena.getStudent())
add.addStudent(maks.getStudent())

add.showGroup()

add.deleteStudent(alex.getStudent())
add.showGroup()