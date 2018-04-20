import csv

from python_basic_course.final_project.utils import *

    #generetad list of 100 dictionaries
ls = []
for i in range(100):
    ls.append(generated_input())

    #create files .csv across call function 'check_credents':
with open ("cardholders.csv", "w", newline= "") as cardholders_csv:
    header = ["Name", "Phone", "Exp_day", "Card"]
    writer = csv.DictWriter(cardholders_csv, fieldnames= header)
    writer.writeheader()
    for i in range(len(ls)):
        if not check_credents(ls[i]):
            writer.writerow({"Name": ls[i].get("Name"), "Phone": ls[i].get("Phone"),"Exp_day": ls[i].get("Exp_day"), "Card": ls[i].get("Card")})

with open("cardholders_errors.csv", "w", newline="") as cardholders_error_csv:
    header = ["Name", "Phone", "Exp_day", "Card"]
    writer = csv.DictWriter(cardholders_error_csv, fieldnames= header)
    writer.writeheader()
    for i in range(len(ls)):
        if check_credents(ls[i]):
            writer.writerow({"Name": ls[i].get("Name"), "Phone": ls[i].get("Phone"), "Exp_day": ls[i].get("Exp_day"), "Card": ls[i].get("Card")})