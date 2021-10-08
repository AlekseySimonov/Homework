while True:
    a = (input('Введите первое число: '))
    b = (input('Введите второе число: '))
    if not a.isdigit():
        print("Введите корректные числа")
    elif not b.isdigit():
        print("Введите корректные числа")
    if a.isdigit():
        a = int(a)
        if b.isdigit():
            b = int(b)
            while a != b:
                if a > b:
                    a = a - b
                else:
                    b = b - a
            print('Наибольший общий делитель: ' + str(a))
