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


        b = len(a)
        for i in range(b-1):
            for j in range(0, b - i - 1):
                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
        print(a, end=".")

