# import os

def card_has_error(number_card): #5167 ..... ......

    list_card_num = number_card.split(" ")
    if len(list_card_num) != 4:
        return False
    for i in list_card_num:
        if len(i) == 4:
            try:
                i = int(i)
            except:
                return False
        else:
            return False
    return True

def print_bank(number):
    if number == "5167":
        return "You use PrivatBank credit card"
    elif number == "5375":
        return "You use Monobank credit card"
    return "You use credit card from the unknown bank"

def experation_date(mm,yy):

    try:
        if not len(mm) == 2 or not len(yy) == 2 or int(mm) < 1 or int(mm) > 12 or int(yy) < 18:  # Проверяем на все возможные ошибки ввода.
            return False
        else:
            return True

    except:
        return False

def cvv_code(cvv):
    try:
        if len(cvv) == 3 and int(cvv) >= 0:
            return True
        else:
            return False
    except:
        return False


# def card_type(region):
#     region = os.environ.get("CARD_TYPE", "Europe")