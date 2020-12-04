import re
import pyperclip

data = pyperclip.paste()
to_miss = 'cid'

list_of_passports = data.split('\n\r\n')

new_list = list_of_passports[0].split(':')
print(new_list)

def validate_passport(passport):
    field_re = r'(...):'
    fields = re.findall(field_re, passport)
    if to_miss in fields and len(fields) == 8:
        return 1
    elif to_miss not in fields and len(fields) == 7:
        return 1
    else:
        return 0

if __name__ == "__main__":
    valid_passports = 0
    for passport in list_of_passports:
        valid_passports += validate_passport(passport)
    print('We have', valid_passports, 'valid passports')