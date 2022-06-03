# список (list) - индексируемый упорядоченный тип данных

# в списках можно добавлять элементы, удалять элементы, заменять элементы

# a = [1, 'string', None, True, False, [1, 2, 3], {'1': 1}, set()]

""" append(element) - добавление элементов в конец списка """
# names = ['Aiazada', 'Bektur', 'Alisher']
# print(names)
# names.append('Asan')
# print(names)

""" insert(index, element) - добавление элементов по индексу """
# names = ['Aiazada', 'Bektur', 'Alisher']
# names.insert(1, 'Abai')
# names.insert(len(names), 'Aman')
# print(names)

""" extend(list) -  расширение списка за счет другого списка """
# products = ['Milk', 'Bread', 'Water']
# products2 = ['Knife', 'Bottle', 'Wine']
# products.extend(products2)
# products.append(products2)
# print(products)

""" замена элементов """
# a = 'AsanAsan' - это строк, а не список(list)
# a[3] = 'g' - Error

# list_ = ['python', 'javascript', 'c#', 'java'] а это уже список(list)
# list_[1] = 'c++'
# print(list_)
 

# list.sort(), sorted()

# numbers = [3, 5, 2, 1, 6]
# numbers.sort() - меняет исходный список
# a = sorted(numbers) - создает новый список на основе старого
# print(numbers)
# print(a)

# names = ['Aiazadaaaaa', 'Bekturaa', 'Alisheraassasdasdasd']
# names.sort(key=len, reverse=True)
# print(names)

# sorted(names, key=len, reverse=True)

""" списки, как и строки имеют срезы и индексацию """
# alp = ['a', 'b', 'c', 'd', 'e']
# slice = alp[0:3]
# print(slice) 


# удаление элементов - clear(), remove(), pop()

# cars = ['Toyota', 'BMW', 'Audi', 'Hyundai']
# cars.pop(1) - удаляет по индексу, по умолчанию - удаляет последний элемент
# print(cars)

# cars = ['Toyota', 'BMW', 'Audi', 'Hyundai']
# # cars.remove('Audi') -  удаляет по значению
# cars.remove('BYD') # Error
# print(cars)


# cars = ['Toyota', 'BMW', 'Audi', 'Hyundai']
# cars.clear()
# print(cars)

# cars = ['Toyota', 'BMW', 'Audi', 'Hyundai']
# print(cars.count('Toyota'))


""" копирование списка """

# a = [1, 2, 3, 4, 5]
# b = a.copy()
# print(id(a))
# print(id(b))
# print(b)

# a = [1, 2, 3, 4, 5]
# b = a # Ссылка на один и тот же объект
# b.pop(3)
# print(id(a))
# print(id(b))

# a = [1, 2, 3, 4, 5]
# b = a[:] 
# d = list(a)
# print(a is b)
# print(id(a), id(b), id(d))


""" циклы """
# многократное выполнение определенного участка кода
# циклы:
# 1 for - цикл работает до тех пор пока не кончатся элементы в итерируем объекте
# 2 while - работает до тех пор пока условие является истиной

# ingredients = ['Колбаса', 'Сыр', 'Тесто', 'Соус']
# ingredients[0] = 1
# ingredients[1] = 2
# ingredients[2] = 3

# for i in ingredients:
#     print(i)

# print(dir([1, 2, 3]))
# types = [1, 'string', [1, 2, 3], {'1': 1}, set(), True, None, (1, 2)]
# iter = []
# not_iter = []
# for t in types:
#     if '__iter__' in dir(t):
#         iter.append(t)
#     else:
#         not_iter.append(t)

# print('Итерируемые объекты', iter)
# print("Неитерируемые объекты",  not_iter)

# emails = ['sanira', 'begimay', 'alina', 'nurayim']
# a = []
# for i in emails:
#     a.append(i + '@gmail.com')
# # sanira @gmail.com
# print(a)

# for переменная in последовательность:
#     операция

# range(start, stop, step) - функция, создающая последовательность чисел/итератор.
# range(stop) 
# a = [1, 2, 3, 4, 5, 6]
# for i in a:
#     print(i)

# for elem in range(5, 20+1):
#     print(elem)

# b = range(10)
# nums = []
# for i in range(10): # for i in range(0, 10, 1):
#     nums.append(i)

# print(nums)


# nums2 = list(range(10))
# print(nums2)


"""
Запросить у пользователя ввести почту 5 раз. При этом нам нужно проверить валидна ли почта: кончается указанная строка на @mail.com. Если почта не валидна, то добавить в конце строки @mail.com. Всю почту сохранить в список mails
"""


# mails = [] # пустой список 
# for i in range(6): # запуск цикла (6 раз)
#     mail = input('Введите почту: ') # запрос информации
#     if '@mail.com' in mail: # проверка, есть ли '@mail.com' внутри полученной инфы (mail)
#         mails.append(mail)
#     else:
#         mails.append(mail+'@mail.com')

# print(mails)

# mails = [] # пустой список 
# for i in range(2): # запуск цикла (6 раз)
#     mail = input('Введите почту: ') # запрос информации
#     if mail[-9:] == '@mail.com': # проверка, есть ли '@mail.com' внутри полученной инфы (mail)
#         mails.append(mail)
#     else:
#         mails.append(mail+'@mail.com')

# print(mails)

# mails = [] # пустой список 
# for i in range(6): # запуск цикла (6 раз)
#     mail = input('Введите почту: ') # запрос информации
#     if mail.lower().endswith('@mail.com'): # проверка, есть ли '@mail.com' внутри полученной инфы (mail)
#         mails.append(mail)
#     else:
#         mails.append(mail+'@mail.com')

# print(mails)


# while условие является истиной:
#     операция

# counter = 0
# while counter < 10:
#     print('Привет')
#     print(counter)
#     # counter = counter + 1
#     counter += 1


# a = list(range(1, 10)) # создали список от 1 до 10
# counter = 0 # счетчик
# while counter < len(a): # условие: пока не counter не сравнится с длиной списка
#     print(a[counter])
#     counter += 1


""" break, continue """

# while True:
#     a = input('Введите слово ')
#     if a == 'stop':
#         break
#     else:
#         print(a)

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in a:
#     if i == 8:
#         break
#     else:
#         print(i)
# for i in a:
#     if i % 2 != 0:
#         print(i)
#     else:
#         continue



