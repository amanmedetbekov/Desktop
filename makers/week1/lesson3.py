# # #логические выражения

# # # операции сравнения
# # # ==, !=, >, <, >=, <=
# # #сравнение строк

# # "!" < "$"
# # "$" < "0"
# # "9" < "A"
# # "A" < "a"


# # str1 = "abcefgaw"
# # str2 = "abd"

# # str1 < str2 #True

# # str1 = 'Hello'
# # str2 = 'hello'

# # str1 < str2

# # letter1 = "A"
# # letter2 = "a"

# # # print(ord(letter1)) #65
# # # print(ord(letter2)) #97

# # print(chr(97)) #a

# # # is - проверяет, что 2 объекта являются одним и тем же объектом

# # # a = 5
# # # print(id(a))

# # # b = 5
# # # print(id(b))

# # # a is b #True

# # a = [1,2,3]
# # b = [1,2,3]

# # print(a is b) #False

# # # in - проверка на вхождение

# # str1 = 'Sample text'

# # letter = 'e'
# # letter2 = 'y'

# # letter in str1 #True
# # letter2 in str1 #False

# # list1 = ['Nikita', 'Maksat', 'Ainura']
# # name1 = 'Maksat'
# # name2 = 'Janylai'

# # name1 in list1 #True
# # name2 in list1 #False

# # # isupper(), islower()

# # a1 = 'Hello world'
# # a2 = 'GOOOO!'

# # a1.isupper() #False
# # a1.isupper() #True

# # # startswith(), endswith()

# # a1 = 'Some dummy text'

# # a1.startswith('s') #False
# # a1.endswith('t') #True
# # a1.endswith('ext') #True

# # #перевод объектов в bool

# # a1 = 10
# # bool(a1) #True

# # # Объекты, которые являются ложными (False)

# # 0, '', [], (), {}, set(), frozenset(), None, False

# # #Все остальные объекты являются истинными

# # -10, 2.5
# # ' ', '\n', '12'
# # [1, 2]
# # (1,)
# # {'a': 1}
# # {1,2}
# # True

# # int(False) #0
# # int(True) #1

# # # if условие:
# # #     действие

# number = 11

# #если число является чётным, то распечатать OK

# # if number % 2 == 0:
# #     print('OK')


# # number = -10

# # if number:
# #     print('Ok')


# name = 'Meerim'
# students_in_class = ['Oksana', 'Janyl', 'Kanat']


# #Если Мээрим в классе, распечатаем 'позвать Мээрим'

# # if name in students_in_class:
# #     print('позвать Мээрим')

# number = int(input('Введите число'))

# #Если число больше 0, то распечатать его корень, в обратном случае распечать нельзя вычислить корень

# from math import sqrt

# if number > 0:
#     print(sqrt(number))
# else:
#     print('нельзя вычислить корень')


# score = 96

# #87 - 100 -> 5
# #74 - 86 -> 4
# #61 - 73 -> 3
# #0 - 61 -> 2 

# if score >= 87:
#     mark = 5
# elif score >= 74:
#     mark = 4
# elif score >= 61:
#     mark = 3
# else: 
#     mark = 2


# # and, or

# temperature = 95
# pressure = 3.5

# #реакция запускается при температуре выше 100 и давлении больше 3

# if temperature > 100 and pressure > 3:
#     print('Реакция запущена')

# price = 25000

# soms = 15000
# rate = 83
# usd = 350

# if soms > price or usd * rate > price:
#     print('Успешная оплата')

# # not - отрицает условие

# # is, is not
# # a is None
# # b is not None

# # in, not in
# # 10 in [10, 20, 30]
# # 10 not in [10,20,30]

# number = 100

# # if number > 50:

# # if not number <= 50:

# number = 0

# if not number:
#     ...


# # and
# # False and False -> False
# # True and False -> False
# # False and True -> False
# # True and True -> True

# number = 10

# #если число является чётным и положительным, распечатать OK

# if number % 2 == 0 and number > 0:
#     print('OK')

# # or
# # False or False -> False
# # True or False -> True
# # False or True -> True
# # True or True -> True

# salary = 50000
# amount = 40000
# price = 85000

# #Если зарплата больше, чем 45000 или первоначальный взнос больше 20%, то кредит одобрен

# if salary >= 45000 or amount > price * 0.2:
#     verified = True

# # not
# # not True -> False
# # not False -> True

# # if условие1 and условие2 and условие3

# # if условие1 or условие2 or условие3

# max_active_ads = 10


# my_active_ads = 9
# 'create', 'open', 'close'

# #Если кол-во открытых объявлений превышает лимит, выдавать сообщение с ошибкой

# if (action in ['create', 'open']) and my_active_ads >= max_active_ads:
#     print('Достигнут лимит')

# #5

# number = input('Введите число или нажмите Enter, чтобы выбрать по умолчанию') or 5
# number = int(number)

number1 = 'abc'