# функция - это именованный блок кода


#объявление функции (definition):
# def  название(параметры):
#     действия(параметры) #тело функции

#вызов функции (call):
# название (аргументы)


# def func1(a, b):
#     res = a+ b
#     print(res)
#     return res
# x = func1(10, 20)
# print(x * 10)  #300


""""""
# назначение функции - переиспользование кода

# a1, a2, a3 = 10, 12, 23
# sqrt(p(p-2)*(p-b)*(p-c))
# # p - половина периметра
# from math import sqrt
# p = (a1 + a2 + a3) / 2
# S = sqrt(p*(p-a1)*(p-a2)*(p-a3))

# b1, b2, b3 = 29, 37, 11
# p = (b1 + b2 + b3) / 2
# S = sqrt(p*(p-b1)*(p-b2)*(p-b3))



""""""
# через def 
# from math import sqrt
# def get_t_area(x, y, z):
#     p = (x + y + z) / 2
#     S = sqrt(p*(p-x)*(p-y)*(p-z))
#     return S

# print(get_t_area(15,20, 26))


""""""
# параметры могут быть обязательные и необязательные (задано значение поумолчанию)


# def my_func(a: int, b: int):  #-> int если ничего не возврашается None
#     '''Функция принимает 2 числа и возвращает их произведение'''
#     res = a * b
#     return res

# # Аргументы бывают позиционные и именованные
# x = my_func(10, 20) #позиционные
# y = my_func(b=20, a=32) #именованные

# x # 200
# y # 640



# # def func1(x: str, y: str) -> str:
# #     return x + y
# # func1(10, 20)
# # func1('a', 'b') """"""
# # func1([1, 2], [3, 4])


# #
# # def func2(a: int, b: int=10)
# #     print(a+b)
#     # return a + b
# # елси func1(10) будет 20, так как в параметре b поумолчанию указана 10
# # fucn2(a=2, 21) #Ошибка




# def m(nums: list) -> int:
#     '''Приниает неограниченное кол-во чисел и 
#     переумн-ет их между собой. Возвр-т рез-т переумн-я'''
#     total = 1 
#     for num in nums:
#         total *= num
#         return total

# m([10, 20, 30, 45])
# m((20, 30, 45, 85))




# def m1(*args):  #необязательно *args, можно и *nums и тд
#     total = 1 
#     for num in args:
#         total *= num
#     return total
# print(m1(11, 20, 30, 45))


# def some(a, b, *args):
#     pass
# some(10, 20, 30, 40, 50)
# #a 10
#b 20
#args (30, 40, 50)

# def some1(a, b, **kwargs):
#     pass
# some1(a=10, b=20, c=30, d=40)
#a 10
#b 20
#kwargs ("c": 30, "d": 40)


# def s(x: int, y: str) ->str:
#     ss = x + y
#     return ss

# print(s('a', 'v'))

# функция используется, чтобы разделять логику
# (функция должна отвечать за одно действие)





"""Декораторы"""


# def gogog(a, b, c):
#     return 'sada'
# print(gogog())
# d = ' a s d '
# s = '+'.join(d)
# # print(s)


# def get_type(a):
#     for i in a:
#         print(i)
    

# print(get_type([5, 's']))

# num = 7
# def check(a):
#     if a % 2 == 0:
#         return 'It is even number'
#     else:
#         return "It is odd number"
# # print(check(num))
# def w(name, lastname):
#     return f"Привет {name}, по фамилии {lastname}"
# print(w(lastname = 'Пушкин', name = 'Александр'))

