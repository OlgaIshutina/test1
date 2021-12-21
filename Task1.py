# 1.	Напишите программу с классом Student, в котором есть три атрибута: name, groupNumber и age.
# По умолчанию name = Ivan, age = 18, groupNumber = 10A.
# Необходимо создать пять методов: getName, getAge, getGroupNumber, setNameAge, setGroupNumber.
# Метод getName нужен для получения данных об имени конкретного студента, метод getAge нужен
# для получения данных о возрасте конкретного студента, vетод setGroupNumberнужен для получения
# данных о номере группы конкретного студента. Метод SetNameAge позволяет изменить данные атрибутов
# установленных по умолчанию, метод setGroupNumber позволяет изменить номер группы установленный
# по умолчанию. В программе необходимо создать пять экземпляров класса Student, установить им разные имена, возраст и номер группы.

class Student(object):
    name = "Ivan"
    age = 18
    groupNumber = "10A"
    def __init__(self, name,age, groupNumber):
        self.name = name
        self.age = age
        self.groupNumber = groupNumber

    def printinfo(self):
        print(self.name, self.age, self.groupNumber)

    def getName(self):  # Getter
        return self.name
    def getAge(self):  # Getter
        return self.age
    def getGroupNumber(self):  # Getter
        return self.groupNumber

    def setNameAge(self,name, age ):  # Setter
        self.name = name
        self.age = age

    def setGroupNumber(self, groupNumber):  # Setter
        self.groupNumber = groupNumber


Student1 = Student("Olga", 24, "11B")
Student2 = Student("Ivan", 20, "10B")
Student3 = Student("Tim", 29, "9B")
Student4 = Student("Yura", 28, "8B")
Student5 = Student("Oleg", 19, "7B")
print(Student3.getName())
print(Student2.getAge())
print(Student1.getGroupNumber())
Student1.setNameAge("Ilya", 25)
Student1.printinfo()
Student1.setGroupNumber("12A")
Student1.printinfo()