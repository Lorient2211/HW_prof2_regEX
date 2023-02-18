import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", 'r',encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


def phone_cor(contacts_list):
    phone_patt = r'(8|\+7)\s*\(*(\d{3})\)*[\s-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})[\s\(]*(доб.)*\s*(\d*)\)*'
    right_patt = r'+7(\2)\3-\4-\5 \6\7'
    for phone in contacts_list[1:]:
        if phone[5] != '':
            result = re.sub(phone_patt, right_patt, phone[5])
            phone[5] = result
    return contacts_list


