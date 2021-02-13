'''This programm is a solution
for day 4 challenges of Advent of Code 2020:
    validating passport credentials.

Before running this code you should copy your
input data into the clipboard'''

import re
import pyperclip

data = pyperclip.paste()
to_miss = 'cid'

list_of_passports = data.split('\n\r\n') # /r might be specific feature for windows

'''first, let's implement light validation'''
def validate_passport_light(passport):
    field_re = r'(...):'
    fields = re.findall(field_re, passport)
    if to_miss in fields and len(fields) == 8:
        return 1
    elif to_miss not in fields and len(fields) == 7:
        return 1
    else:
        return 0


'''now let's implement hard validation:
let's define validation functions for each field'''   

def val_byr(passport):
    check_re = r'byr:([\d]{4})'
    value = re.findall(check_re, passport)
    if value != []:
        if int(value[0]) >= 1920 and int(value[0]) <= 2002:
            return True
        else:
            return False
    else:
        return False
    
def val_iyr(passport):
    check_re = r'iyr:([\d]{4})'
    value = re.findall(check_re, passport)
    if value != []:
        if int(value[0]) >= 2010 and int(value[0]) <= 2020:
            return True
        else:
            return False
    else:
        return False
    
def val_eyr(passport):
    check_re = r'eyr:([\d]{4})'
    value = re.findall(check_re, passport)
    if value != []:
        if int(value[0]) >= 2020 and int(value[0]) <= 2030:
            return True
        else:
            return False
    else:
        return False

def val_hgt(passport):
    check_cm_re = r'hgt:([\d]+)([ci][mn])'
    value = re.findall(check_cm_re, passport)
    if value != []:
        height = int(value[0][0])
        unit = value[0][1]
        if unit == 'cm' and height >= 150 and height <= 193:
            return True
        elif unit == 'in' and height >= 59 and height <= 76:
            return True
        else:
            return False
    else:
        return False

def val_hcl(passport):
    check_re = r'hcl:(#[a-z|\d]{6})'
    value = re.findall(check_re, passport)
    if value != []:
        return True
    else:
        return False

def val_ecl(passport):
    check_re = r'ecl:([a-z]{3})'
    check_list = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    value = re.findall(check_re, passport)
    if value != []:
        if value[0] in check_list:
            return True
        else:
            return False
    else:
        return False

def val_pid(passport):
    check_re = r'pid:(\d+)'
    value = re.findall(check_re, passport)
    if value != []:
        if len(value[0]) == 9:
            return True
        else:
            return False
    else:
        return False

validation_functions = [val_byr, val_iyr, val_eyr, val_hgt, val_hcl, val_ecl, val_pid]

'''and combine them into hard validation function'''
def validate_passport_hard(passport):
    for val in validation_functions:
        if val(passport):
            pass
        else:
            return 0
    return 1


if __name__ == "__main__":
    valid_passports_light = 0
    valid_passports_hard = 0
    for passport in list_of_passports:
        valid_passports_light += validate_passport_light(passport)
        if True:
            valid_passports_hard += validate_passport_hard(passport)
    print('We have', valid_passports_light, 'valid passports according to light validation')
    print('We have', valid_passports_hard, 'valid passports according to hard validation')
