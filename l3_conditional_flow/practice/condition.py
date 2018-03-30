name = input("Enter your name:\n")
age = input("\n" "Enter your age:\n")
email = print("\n"f'Your email {name + age}@itea.ua' '\n')
try:
    name/input("Enter something value:\n")
    surname = print("\nNoob")
except TypeError:
    surname = print("\n""Marlin")
print("\nDeveloping with Python...\n")

if surname=="Noob":
    print("Ti dopustil oshibku!")
else:
    print("Molodec")

### К домашнему заданию:

# number=input("Enter Credit card number!\n(Attention: 16 digits.):\n\n")
# long=len(number)
# try:
#     number=int(number)
#     if long!=16 or number<0:
#         print("!!!")
#         exit()                              #можно воспользоваться таким вариантом:   raise ValueError("Long format")
# except ValueError:                          #можно воспользоваться таким вариантом:   except ValueError as error:
#     print("Not the correct format!")        #можно воспользоваться таким вариантом:   print("Not the correct format!" + repr(error))
#     exit()