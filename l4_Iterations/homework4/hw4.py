while True:
    number_card = str(input("Enter Credit card number in format: **** **** **** ****\n(Attention: 16 digits.):\n\n"))              # Вводим номер карты.
    list_card_num = number_card.split(" ")
    u = True
    if len(list_card_num) != 4:
        continue
    for i in list_card_num:
        if len(i) == 4:
            try:
                i = int(i)
            except:
                u = False
                break
        else:
            u = False
            break
    if u != True:
        continue
    if list_card_num[0] == "5167":
        print("You use PrivatBank credit card")
    elif list_card_num[0] == "5375":
        print("You use Monobank credit card")
    else:
        print("You use credit card from the unknown bank")
    break
while True:
    try:
        mm, yy = input("\nExperation date your card in format \"mm/yy\":\n\n").split("/")
        if not len(mm) == 2 or not len(yy) == 2 or int(mm) < 1 or int(mm) > 12 or int(yy) < 18:  # Проверяем на все возможные ошибки ввода.
            continue
        else:
            break

    except:
        continue
while True:
    try:
        cvv = input("\nEnter secret key:\n\n")
        if len(cvv) == 3 and int(cvv) >= 0:
            break
        else:
            continue
    except:
        continue