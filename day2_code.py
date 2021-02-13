'''This programm calculates the answer
for day 2 challenges of Advent of Code 2020'''

import re


def get_input_lines(input_data):
    '''extraact lines from input text'''
    line_re = r'(\d.+)'
    input_lines = re.findall(line_re, input_data)
    return input_lines


def verify_password_old(input_line: str):
    '''
       Verifies if the password is valid in each policy+password line
       according to the old policies (Task 1)
       Returns 1 for valid policy+password line and 0 for not valid one.
    '''
    min_re = r'([\d]+)-'
    max_re = r'-([\d]+) '
    letter_re = r' ([a-z]):'
    password_re = r'[a-z][a-z]+'
    min_value = int(re.findall(min_re, input_line)[0])
    max_value = int(re.findall(max_re, input_line)[0])
    letter = re.findall(letter_re, input_line)[0]
    password = re.findall(password_re, input_line)[0]
    rule_re = fr'{letter}'
    result = re.findall(rule_re, password)
    if len(result) >= min_value and len(result) <= max_value:
        return 1
    return 0


def verify_password_new(input_line):
    '''
       Verifies if the password is valid in each policy+password line
       according to the new policies (Task 2)
       Returns 1 for valid policy+password line and 0 for not valid one.
    '''
    position_one_re = r'([\d]+)-'
    position_two_re = r'-([\d]+) '
    letter_re = r' ([a-z]):'
    password_re = r'[a-z][a-z]+'
    position_one = int(re.findall(position_one_re, input_line)[0]) - 1
    position_two = int(re.findall(position_two_re, input_line)[0]) - 1
    letter = re.findall(letter_re, input_line)[0]
    password = re.findall(password_re, input_line)[0]
    if password[position_one] == letter and password[position_two] == letter or password[position_one] != letter and password[position_two] != letter:
        return 0
    return 1


if __name__ == "__main__":
    with open('day_2_passwords.txt','r') as file:
        data = file.read()
    lines = get_input_lines(data)
    GOOD_PASSWORDS_OLD = 0
    GOOD_PASSWORDS_NEW = 0

    for line in lines:
        GOOD_PASSWORDS_OLD += verify_password_old(line)
        GOOD_PASSWORDS_NEW += verify_password_new(line)

    print('According to the old policies we have', GOOD_PASSWORDS_OLD, 'valid passwords')
    print('According to the new policies we have', GOOD_PASSWORDS_NEW, 'valid passwords')
