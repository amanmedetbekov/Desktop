# # #переменные

# # x = "Hello world"
# # x2 = 1
# # x3 = [1,2,3]
# # x4 = True

# # x4 = None

# # x1 = 2
# # x2 = 2.5

# # result = x1 + x2
# # print(result)

# # x1 = 10
# # x2 = 3

# # # + -> сложение
# # x1 + x2 #13 

# # # - -> вычитание
# # x1 - x2 #7
# # # /
# # x1 / x2 #3.33333333....

# # # * -> умножение
# # x1 * x2 #30

# # # // -> целочисленное деление (деление по модулю, нахождение целой части от деления)

# # x1 // x2 #3

# # # % -> остаток от деления
# # x1 % x2 #1

# # # ** -> возведение в степень
# # x1 ** x2 #1000

# # pow(x1, x2) #1000


# # num1 = 10
# # num2 = -5

# # # abs() -> модуль числа
# # print(abs(num1))
# # print(abs(num2))

# # # round(дробное_число) -> округление
# # a1 = 2.665
# # round(a1) #3

# # a2 = 3.161
# # round(a2, 2) #3.16

# # a3 = 45.661
# # round(a3, 1) #45.7

# # a4 = 3.275
# # print(round(a4, 2))

# # #дробные числа могут терять точность

# # a1 = 0.7
# # a2 = 0.1

# # print(a1 + a2)

# # #для точных расчётов используется Decimal
# # from decimal import Decimal

# # a1 = Decimal('0.1')
# # a2 = Decimal('0.7')

# # print(a1 + a2)

# # import math

# # a1 = 81
# # print(math.sqrt(a1))

# # # math.sin()
# # # math.cos()

# # #округление
# # math.floor(num1) #округляет вниз
# # math.ceil(num1) #округляет вверх

# # #Операции сравнения

# # # == равно
# # # != неравно
# # # >  больше
# # # <  меньше
# # # >= больше или равно
# # # <= меньше или равно

# # x1 = 28
# # x2 = 34

# # x1 == x2 #False
# # x1 != x2 #True
# # x1 > x2 #False
# # x1 < x2 #True
# # x1 >= x2 #False
# # x1 <= x2 #True

# # #операции с присвоением

# # x1 = 10
# # x2 = 12
# # result = x1 * x2
# # result #120

# # x1 = x1 * x2
# # x1 *= x2

# # x1 #120 


# # x1 = x1 + x2
# # x1 += x2

# # x1 = x1 - x2
# # x1 -= x2

# # x1 = x1 * x2
# # x1 *= x2

# # print() #выводит в терминал
# # input() #запрашивает ввод из терминала


# # name = input("Введите имя: ")
# # print(type(name))

# age = int(input("Введите возраст: "))
# print(type(age))

# #правила наименования переменных

# #названия переменных не должны содержать пробелов и спец символов, кроме нижнего подчеркивания

# my age #ошибка
# my-age #ошибка
# my(age #ошибка

# my_age #правильно
# myAge #допустимо

# #название переменной не может начинаться с цифры

# 1num #ошибка
# num1 #правильно

# #название переменной должно содержать только строчные символы (не обязательно)

# название переменной(функции) не должно совпадать с названием встроенных функций (операторов)

input = 10
print = 20

print(10 * 20)

# название переменной не может быть латинскими буквами l или o (необязательно)
#название переменной должно содержать только латинские символы

l = 20


a = 'Adilet'
x = 'Adilet'

name = "Adilet"