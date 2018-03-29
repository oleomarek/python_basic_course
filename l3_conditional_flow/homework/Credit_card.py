nomber=input("Enter Credit card nomber!\n(Attention: 16 digits.):\n\n")
long=len(nomber)
try:
    int(nomber)
except ValueError:
    print("Not the correct format!")
    nomber = input("Enter your card nomber again!\n(Attention: 16 digits.):\n\n")
    long = len(nomber)
    try:
        nomber=int(nomber)
    except ValueError:
        exit()

if long==16:
    #string>=len(nomber)
    print("Ok")
else:
    exit()
    #print(long)

    #try:

mm=int(input("\nEnter month:\n\n"))
#print(mm)
"""try:
    mm>12
    print("Noob")
except ValueError:
    print("Ok")"""

yy=int(input("\nEnter year:\n\n"))
period=print(mm, yy,sep="/")
try:
    period=int(period)
    exit()
except TypeError:
    print("Ok")

#period=int(input("\nEnter validity period of the card in format mm/yy:\n\n"))
cvv=input("\nEnter CVV key:\n\n")
if len(cvv)!=3:
    print("Error")
else:
    print("Ha - ha - ha. Now I will use your credit card!")