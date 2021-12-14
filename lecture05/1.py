import random

f1 = open('task1.txt','r')
a = []
for line in f1:
    a.append(int(line.strip('\n')))
    print(a)

b = len(a)
for i in range(0, b):
    for j in range(0, b):
        for k in range(0, b):
            i = random.choice(a)
            j = random.choice(a)
            k = random.choice(a)
            if int(i) + int(j) + int(k) == 2020:
                print(int(i), int(j), int(k))
                print(int(i) * int(j) * int(k))
                f2 = open('output1.txt', 'w')
                f2.write(str(int(j) * int(i) * int(k)))
