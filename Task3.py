# 3.	Создайте класс для подсчета максимума из четырех аргументов,
# минимума из четырех аргументов, средне- арифметического из четырех аргументов,
# факториала аргумента. Функциональность надо реализовать в виде статических методов.

import math
class Math():
    @staticmethod
    def maxof(one, two, three,four):
        return max(one, two, three,four)

    @staticmethod
    def minof(one, two, three,four):
        return min(one, two, three, four)

    @staticmethod
    def sred(one, two, three,four):
        return (one + two + three + four)/4
    @staticmethod
    def factor(num):
        return math.factorial(num)
