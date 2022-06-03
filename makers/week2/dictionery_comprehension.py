# nums3 = ['четное' if num % 2 == 0 else 'нечетное' for num in range(1, 10)]
# print(nums3)
# nums4 = ['четное' if num % 2 == 0 else 'нечетное' for num in range(1, 20) if num > 5]
# print(nums4)

# slovo = input("")
# s1 = len([x for x in slovo if x not in 'aeuoiy'])


# num = [[1, 2], [12, 23], [3, 5]]
# num2 = [h for l in num for h in l]
# print(num2)

# a = [1, 3, 5]
# valii = []
# for value in a:
#     print(value)

# dict1 = {1: 'string', 45: 'jad'}

# b = {key: value for key, value in dict1.items()}
# print(b)
# d  = {2: None, 3: None, 4: None}
# a = {}

# string = input()
# a = sum([1 for i in string if i not in 'aouiye'])
# print(a)

# age_skil = [[55, 8], [23, 4], [76, 5], [43, 6], [56, 7]]

# p = ['senior' if s[0] >= 55 and s[1] > 7 else 'junior' for s in age_skil]

# # print(p)




# v = ['senior' if key>=55 and value>7 else 'junior' for key, value in age_skil]
# print(v)



# students = {'Tilek': 70, 'Mayram': 68, 'Kayrat': 89, 'Meerim': 45, 'Zhibek': 71}
# s = {key:'otlichnik' if value > 70 else 'dvoechnik' for key, value in students.items()}
# print(s)

# names_list = ['Alex', 'John', 'Max', 'Olivia', 'Ellie']
# names_list_sort = [name for name in names_list if name[0].lower() in ('aoeyui')]
# print(names_list_sort)


# names_list = ['Alex', 'John', 'Max', 'Olivia', 'Ellie']
# app = []
# names_list_sort = [n for n in names_list if n[0] in 'AOUEIY']
# print(names_list_sort)



# a = {'Sam': {'math': 95, 'literature': 88}, 'Alice': {'math': 70, 'literature': 98}}
# b = {k: { k1: v1 + 2 for k1, v1 in v.items()} for k, v in a.items()}
# print(b)

# numbers = list(range(1,10))
# n = set(i ** 2 if i % 2 == 0 else i * 3 for i in numbers)
# print(n)

# h = input('Введите: ')
# l = len([s for s in h.lower() if s in 'aoiuye'])
# print(l)
 
f = {k: k*k for k in range(6)}
print(f)
