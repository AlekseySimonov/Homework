while True:
    a = (int(input('Введите первое число: ')))
    b = (int(input('Введите второе число: ')))
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    print(a)