

# from ast import comprehension


# list comprehension используется только если в итоге нужен новый список 

# a = [1, 2, 3, 4, 5]
# for i in a:
#     print(i**2)
# res = []
# # for i in a:
# #     res.append(i**2)
# # res = [i ** 2 for i in a if ...]


# # dict comprehension используется только если в итоге нужен новый словарь

# # list1 = [1, 2, 3, 4, 5]
# # например нужно получить словарь {1: 1, 2: 4, 3:9, 4: 16, 5: 25}
# # решение:
# # # res = {k: k**2 for k in list1}
# # a = {'meat': 100, 'milk': 40, 'bread': 15, 'cheese': 200, 'butter': 160}
# # b = {k: v for k, v in a.items() if v > 150}

# # a = {'meat': 100, 'milk': 40, 'bread': 15, 'cheese': 200, 'butter': 160}

# # # замена значений словаря: если число >= 40 заменить на 1. иначе на -1
# # # реш:
# # b =  {k: 1 if v >= 40 else -1 for k, v in a.items()}
# # print(b)


# v = {'Max': 
#           {'history': 95, 'math': 95, 'lit': 89}, 
# 'Olga': {'history': 81, 'math': 80, 'lit': 89}
# # }

# res = {}

# for name, marks in v.items():
#     max_sumject = ''
#     max_score = 0
#     for subject, score in marks.items():
#         if max_score < score:
#             max_sumject = subject
#             max_score = score
#     res[name] = max_sumject
#     print(res)


# # for name, marks in v.items():
# #     sub = ''
# #     for subject, score in marks.items():
# #         if score == max(marks.values()):
# #             sub = subject
# #     res[name] = sub

# #решение через dict comprehension
# # c = {name: subject for name, marks in v.items() for subject, score in marks.items() if score == max(marks.values())}

# # print(c)

# # другое решение
# # c2 = {name: max(marks, key=marks.get) for name, marks in v.items()}
# # print(c2)

# # max(a, key=) изучить подробнее!!!!!!!!




# dict1 = {100: 'hello', 201: 'ok', 300: 'please'}

# res = {k: len(v) if k % 2 == 0 else len(v) ** 3 for k, v in dict1.items()}


# a = [10, 45, 53, 42, 44, 76, 12, 11, 90, 87]
#если число кратно 56, то умножить на 10 и вывести результат (использовать continue)
# for num in a:
#     if num % 5 != 0:
#         continue
#     print(num * 10)
# a = [10, 21, 34, 21, 28, 87]
# #посчитать сумму чисел до первого отрицательного числа
# total = 0
# for num in a:
#     if num < 0:
#         break
#     total += num
# print(total)



# total2 = 0
# while True:
#     n = int(input())
#     if n == 0:
#         break
#     total2 += n 

# set comprehension

# dict_ = {i for i in range(1, 11)}
# print(dict_)


e = [1, 2, 3, 4, 1, 2]
a = ''
ss = 0
for f in e:
    if f > ss:
        ss = f
print(ss)
