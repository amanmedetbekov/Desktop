print(f'Операции для выполнения: \n + - Сложение\n - - Вычитание\n * - Умножение\n / - Деление (классическое или истинное деление)\n  // - Деление с округлением вниз.\n % - Деление по модулю (вычисляет остаток от деления)\n ** - Возведение в степень.\n sqrt - Квадратный корень из числа')

while True: 
    print('\nКоманда "Stop" для остановки\n')

    oper = ['+', '-', '*', '/', '%', '**', '//', 'sqrt']
    a1 = input('Введите первое число: ')
    if a1 == 'Stop':
        break


    action = input(f'Выберите опреацию:\n')
    if action in oper and action == 'sqrt':
        sqrt_ = int(a1) ** 0.5
        print(f'Итого: {sqrt_}')
        continue
    if oper == 'Stop':
        break

    b1 = input('Введит второе число: ')
    if b1 == 'Stop':
        break


    if a1.isdigit() and b1.isdigit():
        a = float(a1)
        b = float(b1)

        if action in oper and action == '+':
            print(f'Итого: {a+b}')
        elif action in oper and action == '-':
            print(f'Итого: {a-b}')
        elif action in oper and action == '*':
            print(f'Итого: {a*b}')
        elif action in oper and action == '/':
            print(f'Итого: {a/b}')
        elif action in oper and action == '%':
            print(f'Итого: {a%b}')
        elif action in oper and action == '**':
            print(f'Итого: {a**b}')
        elif action in oper and action == '//':
            print(f'Итого: {a//b}')
        else:
            print('Данной операции нет в системе!')
        
    else:
        print('Вы ввели не правильно! Попробуйте снова.')
        


    

