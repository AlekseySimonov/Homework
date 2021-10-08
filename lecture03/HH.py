while True:
    n = input('\n Введите число большее или равное 2: ')
    if not n.isdigit():
        print("Введите корректное число")
    if n.isdigit():
        n = int(n)
        if n < 2:
            print('Введено некоректное число')
        a = [b for b in range(n + 1)]
        a.remove(0)
        a.remove(1)
        print(a, end=" ")


