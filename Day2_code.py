'''This programm calculates the answer
for day 2 challenges of Advent of Code 2020.

Before running this code you should copy your
input data into the clipboard'''

import re
import pyperclip

data = pyperclip.paste()

line_re = r'(\d.+)'
input_lines = re.findall(line_re, data)

def verify_password_old(line: str):
    '''
       Verifies if the password is valid in each policy+password line
       according to the old policies (Task 1)
       Returns 1 for valid policy+password line and 0 for not valid one.
    '''
    min_re = r'([\d]+)-'
    max_re = r'-([\d]+) '
    letter_re = r' ([a-z]):'
    password_re = r'[a-z][a-z]+'
    min_value = int(re.findall(min_re, line)[0])
    max_value = int(re.findall(max_re, line)[0])
    letter = re.findall(letter_re, line)[0]
    password = re.findall(password_re, line)[0]
    rule_re = fr'{letter}'
    result = re.findall(rule_re, password)
    if len(result) >= min_value and len(result) <= max_value:
        return 1
    else:
        return 0
    
def verify_password_new(line):
    '''
       Verifies if the password is valid in each policy+password line
       according to the new policies (Task 2)
       Returns 1 for valid policy+password line and 0 for not valid one.
    '''
    position_one_re = r'([\d]+)-'
    position_two_re = r'-([\d]+) '
    letter_re = r' ([a-z]):'
    password_re = r'[a-z][a-z]+'
    position_one = int(re.findall(position_one_re, line)[0]) - 1
    position_two = int(re.findall(position_two_re, line)[0]) - 1
    letter = re.findall(letter_re, line)[0]
    password = re.findall(password_re, line)[0]
    if password[position_one] == letter and password[position_two] == letter:
        return 0
    elif password[position_one] != letter and password[position_two] != letter:
        return 0
    else:
        return 1    
    
if __name__ == "__main__":
    good_passwords_old = 0
    good_passwords_new = 0
    for line in input_lines:
        good_passwords_old += verify_password_old(line)
        good_passwords_new += verify_password_new(line)
    print('According to the old policies we have', good_passwords_old, 'valid passwords')
    print('According to the new policies we have', good_passwords_new, 'valid passwords')
    

