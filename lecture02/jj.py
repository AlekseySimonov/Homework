while True:
        a = input("Введите целое число от 0 до 99: ")

        if not a.isdigit():
            print("Введите корректное число")

        if a.isdigit():
            a = int(a)
            if 0 <= a <= 19:
                if a == 0:
                    print("ноль")
                elif a == 1:
                    print("один")
                elif a == 2:
                    print("два")
                elif a == 3:
                    print("три")
                elif a == 4:
                    print("четыре")
                elif a == 5:
                    print("пять")
                elif a == 6:
                    print("шесть")
                elif a == 7:
                    print("семь")
                elif a == 8:
                    print("восемь")
                elif a == 9:
                    print("девять")
                elif a == 10:
                    print("десять")
                elif a == 11:
                    print("одиннадцать")
                elif a == 12:
                    print("двенадцать")
                elif a == 13:
                    print("тринадцать")
                elif a == 14:
                    print("четырнадцать")
                elif a == 15:
                    print("пятнадцать")
                elif a == 16:
                    print("шестнадцать")
                elif a == 17:
                    print("семнадцать")
                elif a == 18:
                    print("восемнадцать")
                elif a == 19:
                    print("девятнадцать")
            elif 20 <= a <= 99:
                a = str(a)
                if int(a[0]) == 2:
                    print("двадцать ", end="")
                elif int(a[0]) == 3:
                    print("тридцать ", end="")
                elif int(a[0]) == 4:
                    print("сорок ", end="")
                elif int(a[0]) == 5:
                    print("пятьдесят ", end="")
                elif int(a[0]) == 6:
                    print("шестьдесят ", end="")
                elif int(a[0]) == 7:
                    print("семьдесят ", end="")
                elif int(a[0]) == 8:
                    print("восемьдесят ", end="")
                elif int(a[0]) == 9:
                    print("девяносто ", end="")

                if int(a[1]) == 0:
                    print("")
                elif int(a[1]) == 1:
                    print("один")
                elif int(a[1]) == 2:
                    print("два")
                elif int(a[1]) == 3:
                    print("три")
                elif int(a[1]) == 4:
                    print("четыре")
                elif int(a[1]) == 5:
                    print("пять")
                elif int(a[1]) == 6:
                    print("шесть")
                elif int(a[1]) == 7:
                    print("семь")
                elif int(a[1]) == 8:
                    print("восемь")
                elif int(a[1]) == 9:
                    print("девять")
            else:
                print("Введите корректное число")
