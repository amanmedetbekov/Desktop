"""STRING"""
"""Методы"""


""".find()"""
#Поиск подстроки в строке (первое вхождение)

#string = 'Hello Makers' 
# string = 'Hello Makers'
# print(string.find('H')) #0
# print(string.find('Hello')) #0 потому что возвращает только номер первого вхождения 
# print(string.find('s')) #11 потому что 's' под индексом 11

""""""
# string1 = "Подстановку данных в строки можно осуществить с помощью форматирования строк"
# a = string1.find("е")
# print(a) #38



""".rfind()"""
#Поиск подстроки в строке (последнее вхождение)

# string = 'abcdefghia'
         #0123456789
# print(string.rfind('a')) #9 





""".index()"""
#Метод .index() ищет указанную подстроку в строке, возвращает индекс первого вхождения
# в случает отсутствия вызывает ValueError
# например:
# string = 'Hello'
#          #01234
# print(string.index('Hel')) #0 ('H' под индексом 0. Ищет только по первому символу подстроки)
# print(string.index('фф')) #1 ('e' под индексом 1)
# print(string.index('l')) #2 (в строке два 'l'. возвращает только первое вхождение. Первый 'l' находится под индексом 2)



""".rindex()"""
#Поиск подстроки в строке. Возвращает номер последнего вхождения или вызывает ValueError
# string = 'Hello'
# print(string.rindex('l')) #3 (также как и с .index(), только этот метод возвращает номер последнего вхождения)
# print(string.rindex('a'))




""".replace()"""
#Заменяет символ в строке, но сохранть надо в новой переменной
# string = 'Hello'
# a = string.replace('H', 'M') #заменяем 'H' на 'M'
# print(a) #Mello



""" ''.join() """
# ''.join()



# a = ['a', 's', 'ss']
# s = ''.join(a)
# print(s)


from functools import reduce


list1 = [1, 2, 3, 4]
list_ = [3, 2, 1, 0]
list2 = list(reduce (list1))
print(list2)









