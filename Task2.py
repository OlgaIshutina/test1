# 2.	Напишите программу с пустым классом Country.
# Опишите наследуемые от класса Country классы Russia, Canada, Germany.
# Добавьте каждому классу поле population и опишите метод setPopulation и getPopulation.
class Country():
    pass
class Russia(Country):
    def __init__(self, population):
        self.population = population
    def printinfo(self):
        print(self.population)
    def setPopulation(self, population):
        self.population = population
    def getPopulation(self, population):
        return self.population
class Canada(Country):
    def __init__(self, population):
        self.population = population
    def printinfo(self):
        print(self.population)
    def setPopulation(self, population):
        self.population = population
    def getPopulation(self, population):
        return self.population
class Germany(Country):
    def __init__(self, population):
        self.population = population
    def printinfo(self):
        print(self.population)
    def setPopulation(self, population):
        self.population = population
    def getPopulation(self, population):
        return self.population