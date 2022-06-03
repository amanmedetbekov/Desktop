print('Задание 3')

import random

start = input(f'Введите "+", чтобы начать: ')


while True:
    p = ['Камень', 'Ножница', 'Бумага']
    print('Введите "-", чтобы остановить игру\n')
    me = input("Ваш выбор: ")
    comp = random.choice(p)
    w = 'Вы выиграли!'
    d = 'Ничья!'
    l ='Вы проиграли!'
    print(f'Выбор компьютера {comp}')

    #Все победы
    if comp == p[0] and me == p[1]:
        print(w)
    elif comp == p[1] and me == p[-1]:
        print(w)
    elif comp == p[-1] and me == p[0]:
        print(w)

    #Все ничьи 
    elif comp == p[1] and me == p[1]:
        print(d)
    elif comp == p[0] and me == p[0]:
        print(d)
    elif comp == p[-1] and me == p[-1]:
        print(d)

#Все проигрыши 
    elif comp == p[0] and me == p[-1]:
        print(l)
    elif comp == p[1] and me == p[0]:
        print(l)
    elif comp == p[-1] and me == p[1]:
        print(l)
    else:
        print('Ошибка. Повторите ещё раз.\n')
#Stop
    if me == '-':
        print('Игра остановлена.')
        break