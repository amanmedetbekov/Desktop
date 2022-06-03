# # # #строки

# # # # Строки используются для хранения текстовой информации

# # # # Строки являются неизменяемым, упорядоченным типом

# # # a = 'my string'
# # # b = "my string"

# # # #docstring (строка документации)
# # # c = '''my string'''
# # # d = """my string"""


# # # lyrics = '''Ooh
# # # Na-na, yeah
# # # I saw you dancing in a crowded room
# # # You look so happy when I'm not with you
# # # But then you saw me, caught you by surprise
# # # A single teardrop falling from your eye'''


# # # def my_func():
# # #     """Принимает 2 целых числа. Производит какие-то вычисления
# # #     И возвращает что-то"""
# # #     ...

# # # str1 = "My string"
# # #        #012345678

# # # #обращение к символу (по индексу)
# # # print(str1[6]) # "i"

# # # #получение среза 
# # # str2 = 'Some text'
# # #        #012345678
    
# # # #в срезах есть 3 параметра: начало(start), конец(stop), шаг(step)

# # # str2[0:4:1] #'Some'

# # # #шаг по умолчанию 1
# # # str2[0:4] #'Some'

# # # #старт по умолчанию 0
# # # str2[:4] #'Some'

# # # #stop по умолчанию равен концу строки
# # # str2[5:9:1] #'text'
# # # str2[5:9] #'text'
# # # str2[5:] #'text'
# # # str2[5::1] #'text'
# # # str2[5::] #'text'

# # # #для получения stop, нужно к start прибавить длину среза

# # # #существуют отрицательные индексы

# # # str1 = "Hello"

# # # print(str1[-2]) #'l'

# # # #обращение к срезам справа налево

# # # str1[-1:-4:-1] #'oll'

# # # #шаг по умолчанию -1
# # # str[-1:-4]
# # # #старт по умолчанию -1
# # # str1[:-4:-1]
# # # #stop по умолчанию равен началу строки

# # # # у строк есть длина

# # # a1 = 'my string'
# # # len(a1) #9

# # # #строки можно складывать (конкатенация)

# # # a1 = 'abc'
# # # a2 = 'def'

# # # a1 + a2 #'abcdef'
# # # a2 + a1 #'defabc'

# # # #проверка на вхождение (можно проверять, присутствует ли определённая подстрока в строке)

# # # a1 = 'Today is a sunny day'

# # # sub1 = 'y'
# # # sub1 in a1 #True

# # # sub2 = 'e'
# # # sub2 in a1 #False

# # # sub3 = 'day'
# # # sub3 in a1 #True

# # # sub4 = 'Day'
# # # sub4 in a1 #False

# # # #строки зависят от регистра

# # # a1 = 'day'
# # # a2 = 'Day'

# # # a1 != a2

# # # # экранирование символов
# # # # '\n' - перенос строки
# # # # '\t' - табуляция
# # # # '\r' - выход из табуляции (возврат каретки)

# # a1 = 'Привет!\n\t\rКак дела?'
# # print(a1)

# # # a1 = 'McDonald's' #ошибка
# # # a2 = "McDonald's"
# # # a3 = 'McDonald\'s'

# # # a4 = 'Компания "Монолит"'
# # # a5 = "Компания \"Монолит\""

# # path = 'C:\\Users\\new'
# # path2 = r'C:\Users\new'
# # print(path2)


# # # методы
# # #методы преобразования строк
# # # replace(), split(), strip(), lower(), upper(), ...

# # # replace() - замена символов

# # a1 = 'This is a test string'

# # result = a1.replace('t', '*')
# # print(result)

# # result2 = a1.replace('is', '_')
# # print(result2)

# # # lower(), upper(), capitalize(), title() - преобразуют регистр

# # # lower() - переводит в нижний регистр

# # a1 = 'hello'
# # a1.lower() #'hello'
# # a1.upper() #'HELLO'

# # a2 = 'Good'
# # a2.lower() #'good'

# # a3 = 'OK'
# # a3.lower() #'ok'

# # # capitalize() - преобразует первую букву в заглавную

# # a = 'moscow'
# # b = 'tilek'
# # c = 'john doe'

# # a.capitalize() #'Moscow'
# # b.capitalize() #'Tilek'
# # c.capitalize() #'John doe'

# # c.title() #'John Doe'

# # #методы проверки строк(возвращают True или False)
# # # islower(), isupper(), isdigit(), startswith(), endswith()

# # a1 = 'hello'
# # a2 = 'Goodbye'

# # a1.islower() #True
# # a2.islower() #False

# # # isdigit(), isalpha()

# # a1 = '100'
# # a1.isdigit() #True

# # a2 = 'A767'
# # a2.isdigit() #False


# # #методы поиска в строке
# # # find(), index(), count()

# a = 'Hello, World! I am Python developer'

# # find() - ищет подстроку, возвращает индекс нахождения

# print(a.find('o')) #4
# print(a.rfind('o')) #31
# print(a.find('i')) #-1

# # index() - ищет подстроку, возвращает индекс нахождения

# print(a.index('o')) #4
# print(a.rindex('o')) #31
# print(a.index('i')) #ошибка

# # count() - возвращает число повторений подстроки


# a = 'Tonight\'s gonna be a good night'

# a.count('on') #2
# a.count('day') #0

# # форматирование(интерполяция)

a1 = 'Бакыт'
amount1 = 1000

result = 'Здравствуйте, ' + a1 + '! ' + 'Спасибо за покупку! Сумма вашего заказа: ' + str(amount1)

print(result)

a2 = 'Мээрим'
amount2 = 1250

# .format()


a3 = 'Айзада'
amount3 = 1400

template = 'Здравствуйте, {name}! Спасибо за покупку! Сумма Вашего заказа: {amount:.2f}'

result1 = template.format(name=a1, amount=amount1)
result2 = template.format(name=a2, amount=amount2)
result3 = template.format(name=a3, amount=amount3)

print(result3)

# f-строки (интерполяция)

name = 'Bakai'
last_name = 'Maksatov'
age = 21
city = 'Bishkek'

result = f'Student: {name} {last_name}. {age} years old. Living in {city}'

x = 25
y = 2

res1 = f'{x} ** {y} = {x ** y}'
print(res1)

current_year = 2022
name = 'Kanyshai'
birth_year = 1992

result = f'{name} is {current_year - birth_year} years old'

str1 = 'hello'

res = f'Capitalized version of {str1} is {str1.capitalize()}'
print(res)

# сравнение строк

a1 = 'Hello' #'oellH'

first = ...
last = ...
center = ...