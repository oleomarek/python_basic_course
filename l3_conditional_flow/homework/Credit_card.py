number=input("Enter Credit card number!\n(Attention: 16 digits.):\n\n")             # Вводим номер карты.
long=len(number)                                                                    # Присваиваем переменной 'long' число - равное длинне номера карты.
try:
    number=int(number)                                                              # Проверяем на ошибки и сравниваем длинну.
    if long!=16 or number<0:
        exit()
except ValueError:
    print("Not the correct format!")
    exit()

mm, yy = input("\nExperation date your card in format \"mm/yy\":\n\n").split("/")       # Методом 'split' задаем значения переменным 'mm' и 'yy'.
try:
    if not len(mm)==2 or not len(yy)==2 or int(mm)<1 or int(mm)>12 or int(yy)<0:    # Проверяем на все возможные ошибки ввода.
        exit()
    else:
        print("\nOk")

except ValueError:
    exit()

cvv=input("\nEnter secret key:\n\n")
if len(cvv)!=3:
    print("\nError!!!")
else:
    print("\nHa - ha - ha. Now I will use your credit card!")