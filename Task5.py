# 5.	Реализуйте класс «Человек». Необходимо хранить в полях класса:
# ФИО, дату рождения, контактный теле- фон, город, страну, домашний адрес.
# Реализуйте методы класса для ввода данных, вывода данных,
# реализуйте доступ к отдельным полям через методы класса.
# Также реализуйте классы наследники Worker, Student. Выполните переопределение методов.

class Human(object):
    def __init__(self, fio, age, number, city, contry, adress):
        self.fio = fio
        self.age = age
        self.number = number
        self.city = city
        self.contry = contry
        self.adress = adress
    def printinfo(self):
        print(self.fio, self.age, self.number, self.city, self.contry, self.adress)

    def setFio(self, fio):
        self.fio = fio
    def getFio(self):
        return self.fio

    def setAge(self, age):
        self.age = age
    def getAge(self):
        return self.age

    def setNumber(self, number):
        self.number = number
    def getNumber(self):
        return self.number

    def setCity(self, city):
        self.city = city
    def getCity(self):
        return self.city

    def setContry(self, contry):
        self.contry = contry
    def getContry(self):
        return self.contry

    def setAdress(self, adress):
        self.adress = adress
    def getAdress(self):
        return self.adress
    def DoWork(self):
        print("живет")

class Worker(Human):
    def DoWork(self):
        print("работает")

class Student(Human):
    def DoWork(self):
        print("учится")

Human1 = Human("Иванов", 55, 12345, "NSK", "Russia", "Lenina, 8" )
Human1.printinfo()
Human1.setNumber(54325)
Human1.printinfo()
print(Human1.getAdress())
Human2 = Worker("Петров", 12, 5455566, "NSK", "Russia", "Lenina, 10")
Human2.DoWork()
Human3 = Student("Петров", 12, 5455566, "NSK", "Russia", "Lenina, 10")
Human3.DoWork()