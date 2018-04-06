from hw5 import card_has_error,print_bank,experation_date,cvv_code
# import os
# os.environ["CARD_TYPE"] = "China"

while True:
    print(("Enter Credit card number in format: **** **** **** ****\n(Attention: 16 digits.):\n\n"))
    number_card = input()
    if card_has_error(number_card):
        break
    else:
        continue
print(print_bank(number_card.split(" ")[0]))

while True:
    print("\nExperation date your card in format \"mm/yy\":\n\n")
    try:
        mm, yy = input().split("/")
        if experation_date(mm, yy):
            break
        else:
            continue
    except:
        continue

while True:
    print("\nEnter secret key:\n\n")
    cvv = input()
    if cvv_code(cvv):
        print("Well Done!")
        break
    else:
        continue