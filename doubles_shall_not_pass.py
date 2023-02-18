import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv
from names import name_changer
from phone import phone_cor



with open("phonebook_raw.csv", 'r',encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

contacts_list = phone_cor(contacts_list)
contacts_list1 = name_changer(contacts_list)

#print(contacts_list1)

def doubles_remuver(contacts_list1):
    dict_names = {}


    for lastname in contacts_list1:
        if lastname[0] not in dict_names.keys():
            dict_names[lastname[0]] = lastname

        else:
            ind = 0
            for gaps in dict_names[lastname[0]]:
                if gaps == '':
                    dict_names[lastname[0]][ind] = lastname[ind]
                ind += 1
    return dict_names.values()


