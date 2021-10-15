import random
while True:
    n = input('\n Введите количество случайных чисел: ')
    if not n.isdigit():
        print("Введите корректное число")
    if n.isdigit():
        n = int(n)
        if  n < 1:
            print("Введите корректное число")
        a = list(range(n+1))
        a.pop(0)
        random.shuffle(a)
        print(a, end=",")
