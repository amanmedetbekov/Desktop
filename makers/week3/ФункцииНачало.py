"""ФУНКЦИИ"""

'''объявления функции:
def function1():  #из переменной создали функцию
    return        
'''

'''вызов функции:
fuction1() #вызвали функцию по имени
'''

# def sub():
#     n1 = 20
#     n2 = 10
#     print(n1 + n2)
#     return n1 - n2
# print(sub())



'функция в функции'

# def sub():
#     n1 = 20
#     n2 = 10
#     return n1 - n2

# def dub(a, b):
#     return a + b

# print(dub(sub(), 5)) #вызвали функцию dub() и в качестве аргумета передали ранее созданную функцию sub() и число 5
# list_ = [1, 2, 3, 4, 5, dub(sub(), 5)] #внутри списка функция в функции
# print(list_)         #[1, 2, 3, 4, 5, 15]




# def sub():
#     n1 = 20
#     n2 = 10
#     print('Tutturuu')
#     return n1 - n2


# def dub():
#     aa = sub()
#     return aa
    
# print(dub())



# def welcome(name1, last_name1):
#     return f'Welcome {name} {last_name}'
# name = input('Enter your name: ')
# last_name = input('Enter your last name: ')

# print(welcome(last_name1=last_name, name1=name))





# def get_word(word):
#     list_letters = list(word)
#     return list_letters

# def get_vowels(let):
#     vowels = 'aeyuio'
#     list_ = [i for i in let if i in vowels]
#     return list_
# slovo = input('Введите слово: ').lower()
# p = get_vowels(get_word(slovo))
# bukvy = ''.join(p)
# print(bukvy)




""" *args, **kwargs"""
#Позволяет функции принимать необязательные аргументы


# def func(a, *args, **kwargs):
#     return a, args, kwargs


# print(func('a', 45, 55, s=5))


# def is_palindrome(a):
#     if str(a).isdigit:
#         d = str(a).lower()
#     if d == d[::-1]:
#         print(True)
#     else:
#         print(False)
# is_palindrome(101)

# def sum_digits(n):
#     l = []
#     for i in str(n):
#         l.append(int(i))
#     number = 0
#     for i in l:
#         number += i
#     return number
# print(sum_digits(106))





