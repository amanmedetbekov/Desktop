# # # # # # #словари
# ​
# # # # # # a = {} #словарь
# # # # # # a1 = set() #множество
# ​
# # # # # # b = dict()
# ​
# # # # b1 = {'a': 1} #словарь
# # #  b2 = {1, 2, 3} #множество
# ​
# # # # # # # словарь - изменяемый и неупорядоченный
# ​
# # # # # # a = {'model': 'Acer Aspire', 'color': 'black', 'ram': 16, 'hdd': 500}
# ​
# # # # # # # ключи должны быть неизменяемыми, также они не могут повторяться
# ​
# # # # # # a = {'a': 1, 'b': 2, 'c': 2, 'a': 4}
# ​
# # # # # # print(a)
# ​
# ​
# # # # # # # можно добавлять, удалять и изменять элементы
# ​
# # # # # # person = {'name': 'Bakai', 'last_name': 'Makaev', 'age': 28}
# ​
# # # # # # # добавление
# # # # # # person['city'] = 'Bishkek'
# ​
# # # # # # print(person)
# ​
# # # # # # # update(dict) - расширяет словарь элементами другого
# ​
# # # # # # person.update({'height': 191, 'age': 29})
# ​
# # # # # # print(person)
# ​
# # # # # # # setdefault(ключ, [значение|None]) - если такого ключа нет, то добавляет элемент c указанным значением (по умолчанию None). Если ключ есть, то ничего не происходит
# # # # # # # 
# ​
# # # # # # person.setdefault('city', 'Karakol')
# # # # # # person.setdefault('weight', 90)
# ​
# # # # # # print(person)
# ​
# # # # # # #удаление
# ​
# # # # # # car = {'model': 'Toyota Camry', 'year': 2015, 'color': 'silver'}
# # # # # # del car['color']
# # # # # # print(car)
# ​
# # # # # # # pop(ключ) - удаляет по ключу
# # # # # # car = {'model': 'Toyota Camry', 'year': 2015, 'color': 'silver'}
# # # # # # deleted = car.pop('color', 'white')
# # # # # # print(deleted)
# # # # # # print(car)
# ​
# # # # # # popitem() - удаляет последний элемент и возращает его в виде кортежа
# # # # # car = {'model': 'Toyota Camry', 'year': 2015, 'color': 'silver'}
# ​
# # # # # deleted = car.popitem()
# ​
# # # # # deleted #('color', 'silver')
# ​
# # # # # print(car)
# ​
# # # # # # clear() - очищает все элементы
# ​
# # # # # dict1 = {'a': 1, 'b': 2, 'c': 3}
# ​
# # # # # dict1.clear()
# ​
# # # # # dict1 #{}
# ​
# # # # # # замена значения
# ​
# # # # # dict1 = {'a': 1, 'b': 2, 'c': 3}
# ​
# # # # # dict1['b'] = 5
# ​
# # # # # print(dict1)
# ​
# ​
# # # # # dict1.update({'b': 10})
# ​
# ​
# # # # # dict1 = {'name': 'A', 'last_name': 'B'}
# ​
# # # # # city = dict1['city']
# ​
# # # # # # get() - позволяет получить значение без ошибки
# ​
# # # # # ed = dict1.get('high_education')
# ​
# # # # # ed #None
# ​
# # # # # ed = dict1.get('high_education', 'KSTU')
# ​
# # # # # ed #'KSTU'
# ​
# ​
# # # # # # a.update({'a': 1, 'b': 2, 'c': 3})
# ​
# ​
# # # # # # keys() - возвращает все ключи
# # # # # a = {'a': 1, 'b': 2}
# ​
# # # # # a.keys() #dict_keys(['a', 'b'])
# ​
# ​
# # # # # # values() - возвращает все значения
# # # # # a = {'a': 1, 'b': 2}
# ​
# # # # # a.values() #dict_values([1,2])
# ​
# # # # # # items() - возвращает ключи и значения в виде кортежей
# # # # # a = {'a': 1, 'b': 2}
# # # # # a.items() #dict_items([('a', 1), ('b', 2)])
# ​
# ​
# # # # # цикл for и словарь
# ​
# # # a = {'x': 10, 'y': 32, 'z': 45}
# ​
# # # # # по умолчанию цикл обходит только ключи
# # # # for i in a:
# # # #     print(i)
# ​
# # # # for i in a.keys():
# # # #     print(i)
# ​
# # # # # обход значений
# # # # for i in a.values():
# # # #     print(i)
# ​
# # # #обход элементов (ключ и значение)
# ​
# # # for i in a.items():
# # #     print(i)
# ​
# ​
# # dict1 = {'a': 1, 'b': 2, 'c': 3}
# ​
# # # вывести квадрат всех значений
# # for i in dict1.values():
# #     print(i ** 2)
# ​
# # # вместо значений записать их квадраты
# # for key in dict1.keys():
# #     value = dict1[key]
# #     dict1[key] = value ** 2
# ​
# # i = ('a', 1)
# # k, v = ('a', 1)
# ​
# # for key, value in dict1.items():
# #     dict1[key] = value ** 2
# ​
# ​
# # a = [1, 5, 3, 10, 12]
# ​
# # for i in a:
# #     if i > 5:
# #         a.pop(i)
# ​
# # for i in range(len(a)):
# #     if a[i] > 5:
# #         a.pop(i)
# ​
# ​
# # a = {'x': 1, 'y': 2, 'z': 1}
# ​
# # # print(list(a.keys())[2])
# ​
# # value = a.pop('x')
# ​
# # print(value)
# ​
# ​
# a = {'a': 1}
# ​
# b = a.copy()
# ​
# print(id(a))
# print(id(b))
# ​
# # Пример: Ввод -> 
# a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6} 
# #  Вывод -> 
# b = {'a': 1, 'b': 2, 'c': 1, 'd': 5,  'e': 2}
# ​
# b = {}
# for key, value in a.items():
#     if value % 2 == 0:
#         b[key] = 2
#     else:
#         b[key] = value
# ​
# a = {'a': 1, 'c': None, 'b': 2, 'd': None}
# ​
# b = a.copy()
# ​
# for k, v in b.items():
#     if v is None:
#         a.pop(k)    
# ​
# print(a)
# ​
# a = {'a': 1, 'b': 2, 'c': 3}
# ​
# # {1: 'a', 2: 'b', 3: 'c'}
# ​
# res = {}
# for k, v in a.items():
#     res[v] = k
# ​
# print(res)
# ​
# ​
# b = dict(a=1, b=2, c=3)
# ​
# ​
# x1 = 1
# y1 = 1
# ​
# x2 = 5
# y2 = 6
# ​
# if x2 - x1 != 0 and y2 - y1 != 0:
#     print('NO')
# else:
#     print('YES')
    