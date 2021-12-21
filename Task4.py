# 4.	Реализуйте класс «Книга». Необходимо хранить в по- лях класса: название книги, ФИО автора,
# год выпуска, название издательства, жанр книги, количество страниц.
# Реализуйте конструкторы и методы класса для ввода данных, вывода данных,
# реализуйте доступ к отдельным полям через методы класса. Используйте механизм пере- грузки методов.

class Book(object):
    def __init__(self, name, fio, age, isdatel, janr, number):
        self.name = name
        self.fio = fio
        self.age = age
        self.isdatel = isdatel
        self.janr = janr
        self.number = number
    def printinfo(self):
        print(self.name, self.fio, self.age, self.isdatel, self.janr, self.number)
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
    def setFio(self, fio):
        self.fio = fio
    def getFio(self):
        return self.fio
    def setAge(self, age):
        self.age = age
    def getAge(self):
        return self.age
    def setIsdatel(self, isdatel):
        self.isdatel = isdatel
    def getIsdatel(self):
        return self.isdatel
    def setJanr(self, janr):
        self.janr = janr
    def getJanr(self):
        return self.janr
    def setNumber(self, number):
        self.number = number
    def getNumber(self):
        return self.number
Book1 = Book("цель", "Иванов", 55, "Азбука","детектив",100)
Book1.setJanr("задача")
Book1.printinfo()
print(Book1.getNumber())