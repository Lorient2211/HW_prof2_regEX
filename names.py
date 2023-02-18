import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", 'r',encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)



def name_changer(contacts_list):

    for names in contacts_list:
        i = 0
        for w in names[0:3]:
            result = re.sub(r' ', ',', w)
            names[i] = result
            i+=1

    for q in contacts_list[1:]:
        counter = 0
        for w in q[0:3]:
            counter += w.count(',')
        if counter == 2:
            q.pop(2)
            q.pop(1)
        elif counter ==1:
            q.pop(2)


    contacts_list1 = []
    for q in contacts_list:
        w = ','.join(q)
        contacts_list1.append(w)

    #print(contacts_list1) ---------------------------------

    ind = 0
    pattern = r'(\w+,)[,?.]*(\w+,)[,?.]*(\w+,)[,?.]*(\w+)'
    right_pattern = r'\1\2\3\4'
    for q in contacts_list1:
        result = re.sub(pattern,right_pattern,q)
        contacts_list1[ind] = result
        ind +=1

    ind = 0
    for q in contacts_list1:
        w = q.split(',')
        contacts_list1[ind] = w
        ind +=1

    return contacts_list1




