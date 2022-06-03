print(f'Операции для выполнения: \n + - Сложение\n - - Вычитание\n * - Умножение\n / - Деление (классическое или истинное деление)\n  // - Деление с округлением вниз.\n % - Деление по модулю (вычисляет остаток от деления)\n ** - Возведение в степень\n sqrt - Квадратный корень из числа')
while True:

    #get the number 1
    def num1(n1=input('Введите первое число: ')):
        if n1.isdigit():
            return int(n1)
        else:      
            return 'Введите цифру, а не буквы!'


    #num1() action num2()
    def action(number_1, oper):
    
        if oper == 'sqrt':
            return f'Итого: {number_1 ** 0.5}'
        
        #get the number 2
        def num2(n2=input('Введите второе число: ')):
            if n2.isdigit():
                return int(n2)
            else:
                return 'Введите число, а не букву!'

        if oper == '+':
            return f'Итого: {number_1 + num2()}'

        elif oper == '-':
            return f'Итого: {number_1 - num2()}'

        elif oper == '*':
            return f'Итого: {number_1 * num2()}'

        elif oper == '/':
            return f'Итого: {number_1 / num2()}'

        elif oper == '%':
            return f'Итого: {number_1 % num2()}'

        elif oper == '**':
            return f'Итого: {number_1 ** num2()}'
        elif oper == '//':
            return f'Итого: {number_1 // num2()}'
        else:
            print ('Данной операции нет в системе!')
        
    print(action(num1(), oper=input('Выберите операцию: ')))
   
    

    
    





