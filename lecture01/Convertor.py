while True:
    i = input( 'Конвертировать \n 1)градусы C в градусы F \n 2)градусы F в C \n 3)выйти из программы \n (1,2,3): ')
    if i == "1":
        a = float( input('Введите градусы С: '))
        c = a*9/5+32
        print('Результат: ' + str(c))
   
    elif i == "2":
        b = float( input('Введите градусы F: '))
        c = (b-32)*5/9
        print('Результат: ' + str(c))
    elif i == "3":
        break

    else:
        print( 'Выбрана неверная операция')
    
     
    






    
    


    
 
        
