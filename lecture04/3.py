import random

n = input('Введите количество чисел: ')

if not n.isdigit():
    print('Введите корректное число')

if n.isdigit():
    n = int(n)
    nums = []
    flag = True

    for i in range(n):
        nums.append(random.randrange(0, 100))

    while flag:
        random.shuffle(nums)
        for i in range(n - 1):
            if nums[i] < nums[i + 1]:
                if i == n - 2:
                    flag = False
            else:
                break
        print(*nums)
