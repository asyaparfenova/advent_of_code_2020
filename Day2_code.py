import re
import pyperclip

data = pyperclip.paste()

#print(data)

line_re = r'(\d.+)'
input_lines = re.findall(line_re, data)

def verify_password(line: str):
    '''Verifies if the password is valid in each policy+password line.
       Returns 1 for valid policy+password line and 0 for not valid one.
    '''
    min_re = r'([\d]+)-'
    max_re = r'-([\d]+) '
    letter_re = r' ([a-z]):'
    password_re = r'[a-z][a-z]+'
    a = int(re.findall(min_re, line)[0])
    b = int(re.findall(max_re, line)[0])
    letter = re.findall(letter_re, line)[0]
    password = re.findall(password_re, line)[0]
    rule_re = fr'{letter}'
    result = re.findall(rule_re, password)
    if len(result) >= a and len(result) <= b:
        return 1
    else:
        return 0
if __name__ == "__main__":
    good_passwords = 0
    for line in input_lines:
        good_passwords += verify_password(line)
    print(good_passwords)
    

