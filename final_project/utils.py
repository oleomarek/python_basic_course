from random import choice
from string import digits
import string
import random
import re

first_name = ("Oleg", "Jenia", "Bogdan", "Andrey", "Daria", "Maria", "Sofia")
last_name = ("Slesarchuk", "Polischuk", "Marlin", "Atamanuk", "Poroshenko", "Dumko", "Polozenko")

error_elm_phone = ("[", "-", "]", " ", str(random.choice(string.ascii_lowercase + string.ascii_uppercase)))
error_elm_card = ("-", " ", str(random.choice(string.ascii_lowercase + string.ascii_uppercase)))
code = "+380"
number = (44, 50, 63, 68, 73, 91, 93, 94, 95)

#function generated Dictionary:
def generated_input():
        #generated key "Name":
    name = (random.choice(first_name)+" "+random.choice(last_name))

        #generated key "Phone":
    phone = list(f"{code}{random.choice(number)}{''.join([random.choice(digits) for x in range(7)])}")
    if random.randint(1, 50) == 1:
        phone[random.randint(1, len(phone)-1)] = random.choice(error_elm_phone)
    phone = ''.join(phone)

        #generetad key "Exp_day":
    mm = str(random.randint(1, 12))
    if len(mm) == 1:
        mm = '0'+ (mm)
    yy = str(random.randint(18, 21))
    exp_day = str(f'{mm}/{yy}')
        #generated key "Card":
    card = list(''.join(choice(digits) for i in range(16)))

    if random.randint(1, 100) == 1:
        card[random.randint(0, len(card)-1)] = random.choice(error_elm_card)
    card = list(map(''.join, zip(*[iter(card)] * 4)))
    card = ' '.join(card)

        #generated Dictionary:
    cardholders = {"Name": name, "Phone": phone, "Exp_day": exp_day, "Card": card}
    return cardholders

#check function phone and card in each dictionary

def check_credents(rand_cred):
    phone_cred = re.match(r'\+\d{12}$', rand_cred.get("Phone"))

    card_cred = re.match(r'\d{4}\ \d{4}\ \d{4}\ \d{4}$', rand_cred.get("Card"))

    if phone_cred and card_cred:

        return True
    else:

        return False