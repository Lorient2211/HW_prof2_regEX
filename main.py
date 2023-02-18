import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv
from names import name_changer
from phone import phone_cor
from doubles_shall_not_pass import doubles_remuver

if __name__ == '__main__':
    with open("phonebook_raw.csv", 'r',encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)

    contacts_list = phone_cor(contacts_list)
    contacts_list1 = name_changer(contacts_list)
    contacts_list1 = doubles_remuver(contacts_list1)



    with open("phonebook.csv", "w", encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(contacts_list1) #используемый список