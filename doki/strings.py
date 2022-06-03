name = 'Python'
version = '3'
result = '{} - {}, {}.'.format(name[0], name, version)
print(result)




string = 'Makers bootcamp'
n = string[1:-1:2]
print(n)


string = 'Hello'
print(string[-1] + string[1:-1:] + string[0])


hashtags = '#makers#bootcamp#программирование#it#курсы'
print(hashtags.lstrip('#').split('#'))