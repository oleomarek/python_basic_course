name = input("Enter your name:\n")
age = input("\n" "Enter your age:\n")
email = print("\n"f'Your email {name + age}@itea.ua' '\n')
try:
    name/input("Enter something value:\n")
    surname = print("\n""Noob")
except TypeError:
    surname = print("\n""Marlin")
print("\nDeveloping with Python...\n")

if surname=="Noob":
    print("Ti dopustil oshibku!")
else:
    print("Molodec")