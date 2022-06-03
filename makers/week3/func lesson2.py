# map 
# filter
# reduce
# all
  




"""map"""

# a = [1, 2, 3, 4]
# def mul(qq):
#     return qq * 2

# c = list(map(mul, a))
# print(c)



# a = [1, 2, 3, 4]
# def mul2(xx):
#     list_ = []
#     for i in xx:
#         list_.append(i * 2)
#     return list_
# print(mul2(a))





# a = [1, 2, 3]
# b  = [4, 5, 6]




# lambda анонимная функция (без имени)





"""filter"""

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# res = list(filter(lambda x: x % 2 == 0, a))
# print(res)






"""reduce"""
# from functools import reduce
# nums = [1, 2, 3, 4, 5, 6]
# c = [10, 11, 12, 13]
# a = reduce(lambda x, y: x*y, nums)
# print(a)


# reduce(func, iterable) -> single value 




# import functools
# nums = [6, 1, 2, 3, 4, 5, 6]
# res = functools.reduce(lambda x, y: x if x < y else y, nums)
# print(res)






"""enumerate"""
# a = 'hello'
# print(list(enumerate(a)))


# for k, c in enumerate(a):
#     print(k, c)
# s = 'hello'
# my_d = dict(enumerate(s))
# print(my_d)


# s = 'world'
# print(list(enumerate(s, 1)))





"""all, any"""
# a = ['jee', 12, [45, 5], {4: 5}]
# print(all(a))


# a = ['', [], False]
# print(any(a))


p = input('enter the passw: ')
print(any(i for i in p if i.isdigit()))




def map_(f, i):
    for a in i:
        yield f
qq = [1, 2, 5]
print()




