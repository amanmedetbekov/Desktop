"""ошибки""" 


""""""
# SyntaxError
# number = 10
# if number%2==0 #не хватает : (это SyntaxError)


""""""
# IndentationError - ошибка отступа

# number = 10
#     if number%2==0:  #IndentationError
#     print('ok') 


""""""
# TabError - если перемешиваются табы и пробелы




"""Исключения"""

""""""
#  ZeroDivisionError - деление на ноль
# a = 10 
# b = 0
# a/b #ZeroDivisionError



""""""
# NameError - не найдено имя (переменная)




""""""
# TypeError - неверный тип
# a = 10
# b = '10'
# print(a+b) #TypeError
# a = [1, 2]
# int(a) # TypeError
# b = 10
# list(b) # TypeError



""""""
# ValueError - объект по типу подходит для операции, но не подходит по значению
# a = '20'
# b = 'abc'
# int(a) #10
# int(b) #ValueError




""""""
# KeyError - несуществующий ключ
# dict1 = {'a': 1, 'c': 5}
# dict1['v']  # KeyError
# dict1.pop('q') # KeyError



""""""
# IndexError - несуществующий индекс
# a = [1, 2, 3]
# a[6] # IndexError



""""""
# AttributeError - несущест. метод или атрибут
# a = (1, 2, 3)
# a.append('s') # AttributeError



""""""
# ModuleNotFoundError 
# from maht import aqrt #  # ModuleNotFoundError нет модуля  maht


""""""
# ImportError
# from test import a
# print(a)
# from test import b




"""Исключения завершают выволнения кода"""
# a1 = 10
# b1 = 'abc'




# try: 
#     ....
# except:
#     ...
#  else: #работает в том случае если в try нет исключений
#     ...
#  finally: #работает в любом случае
#     ...


# a = 10
# a1 = 0
# try:
#   print(a / 0)
# except ZeroDivisionError:
#   print('Произошла ошибка')


# try:
#     print(a/a1)
# except Exception as exc:
#     print(f'Произошла ошибка: {exc}')


# try:
#     a = int(input())
#     a1 = int(input())
#     print(a*a1)
# except ValueError:
#     print('введи число')
# except ZeroDivisionError:
#     print("на 0 не делится")



# try:
#     a = int(input())
#     a1 = int(input())
#     print(a*a1)
# except (ValueError, ZeroDivisionError)
#     print('Ошибка')



# assert - оператор для проверки выражений
# AssertionError



# try:
#     def add(a, b):
#         return a + b
#     def sub(a, b):
#         return a - b
#     def mult(a, b):
#         return a * b
#     def div(a, b):
#         return a / b
#     def kv(a, b):
#         return a ** b
#     def kor(a):
#         return a ** 0,5
#     print('List of operations: +, -, *, /, **, sqrt  \n ')
#     choice = input('Choose an operation: ')
#     num1 = int(input('Enter the first number: '))
#     num2 = int(input('Enter the second number: '))

#     if choice == '+':
#         print(add(num1, num2))
#     elif choice == '-':
#         print(sub(num1, num2))
#     elif choice == '*':
#         print(mult(num1, num2))
#     elif choice == '/':
#         print(div(num1, num2))
#     elif choice == '**':
#         print(kv(num1, num2))
#     elif choice == 'sqrt':
#         print(kor(num1))
# except Exception:
#     print('Value Error! Enter the number!')

# else: 
#     print('Operation completed')
# finally: 
#     print('The end')





try:
    def add(a, b):
        return a + b
    def sub(a, b):
        return a - b
    def mult(a, b):
        return a * b
    def div(a, b):
        return a / b
    def kv(a, b):
        return a ** b
    def kor(a):
        return a ** 0.5

    print('List of operations: +, -, *, /, **, sqrt  \n')

    def num1(a = int(input('Enter the first number: '))):
        return a


    def choice(a = input('Choose an operation: ')):
        if a not in ['+', '-', '*', '/', '**', 'sqrt']:
            print('Error! The operation not in the list of operation')
        else:
            return a

    
    def num2(a = int(input('Enter the second number: '))):
        return a

    def Oper1(num1, choice):

        if choice == 'sqrt':
            return kor(num1)
        
        elif choice == '+':           
            return add(num1, num2())

        elif choice == '-':          
            return sub(num1, num2())

        elif choice == '*':         
            return mult(num1, num2())
        elif choice == '/':
            return div(num1, num2())

        elif choice == '**':
            return kv(num1, num2())

        elif choice == 'sqrt':
            return kor(num1)

    print(Oper1(num1(), choice()))
except Exception:
    print('Enter the correct values')