# try: 
#     database_ = {'ID 123456789': 's@dboy', 'ID 7894561230': 'b@dboy', 'ID 654258789': 'funnyboy', 'ID 753951456852': 'NoIdeaBoy', 'ID 951623847': 'TheEndBoy'}
#     find_user = input('Введите свой username: ')
#     if find_user not in database_.values():
#         print('Введенного юзера нет в базе данных.')
#     else:
#         for k, v in database_.items():
#             if v == find_user:
#                 print(f'user {k}')
#                 print(f'Приветствую, {database_[k]}!')
# except Exception:
#     print(Exception)
# finally:
#     print('Спасибо!')


# database_ = {'ID 123456789': 's@dboy', 'ID 7894561230': 'b@dboy', 'ID 654258789': 'funnyboy', 'ID 753951456852': 'NoIdeaBoy', 'ID 951623847': 'TheEndBoy'}
# find_user = input('Введите свой username: ')

# try:
#     age = int(input('Введите возраст: '))
#     if age <= 0:
#         print('Ваш возраст должен быть больше 0')
#     else:
#         print(f'Вам {age} лет(год)')
# except ValueError:
#     print("Введите число")








# a = {'a': 1, 'b': 5, 'c': 4, 'd': 3}
# # for k, v in a.items():
# #     a[k] = list(range(1, v+1))
# # dict_ = a
# # print(type(dict_))

# dict_ = {k: list(range(1, v + 1)) for k, v in a.items()}
# print(dict_)



# string_ = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
# s = list(string_.split())
# list_ = []
# for i in s:
#     if i.isdigit() == True:
#         list_.append(i)

# print(list_)
# list_ = [i for i in string_.split() if i.isdigit() ]
# print(list_)



# dict_ = {'Timur': {'history': 90, 'math': 95, 'literature': 91},
 
# 'Olga': {'history': 92, 'math': 96, 'literature': 81},
 
#  'Nik':  {'history': 84, 'math': 85, 'literature': 87}}

# max_ = {a: b for a, d in dict_.items() for b, c in d.items() if c == max(d.values())}
# print(max_)


# my_dict = {'first': {'a': 1}, 'second': {'b': 2}}
# dict_ = {k: v1 for k, v in my_dict.items() for k1, v1 in v.items()}
# print(dict_)


# list_ = list(range(11))
# new_list = [i for i in list_ if i % 2 == 0]
# n1 = [i / 2 for i in new_list]
# print(n1)
 



# print('Task 1')
# from random import sample


# def get_password():
#     password = sample(range(0,10), k=7)
#     password = [str(i) for i in password]
#     password = ''.join(password)
#     return password
# get_password()



# def get_info(passw, name = input('Enter your name: '), 
#             last_name = input('Enter your last name: ')):  
#         nl = name + last_name + ''.join(passw)
#         return nl 


# print(get_info(get_password()))

# flavor = input('Вкус: ')
# size = input('Размер: ')
# topping = input('Состав: ')


# def func(a, b, *args):
#   return f'Мороженое {a}, размер {b}, топпинг: {args}' 
# print(func(flavor, size, topping))

# s = list(input('ss '))
# print(s) 


# A = list(map(str, input('VV ')))
# print(A)
        



# students = [{'name': 'jane', 'group': 'python'}, 
#             {'name': 'joe', 'group': 'js'}, 
#             {'name': 'jack', 'group': 'python'}]


# def d(a):
#     for i in a.values():
#         if i == 'python':
#             return a

# g = list(filter(d, students))
# print(g)
# nr = list(filter(lambda x: x['group'] == 'python', students))
# print(nr)



from functools import reduce

def add(a, b):
    return a + b
list_ = [1, 2, 3, 4, 1]
l = [2, 3, 5]
d = [reduce(add, list_)]
d1 = reduce(lambda a, b: 'hi' if a > b else b, list_)
print(d1)

# def add(x, y): 
#     return x + y 
 
# list = [2, 4, 7, 3] 
# print(reduce(add, list)) 