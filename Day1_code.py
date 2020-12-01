'''This programm calculates the answer
for day 1 challenges of Advent of Code 2020.

Before running this code you should copy your
input data into the clipboard'''

import re
import pyperclip

data = pyperclip.paste()

num_re = r'([0-9]+)'
input_numbers = re.findall(num_re, data)

def find_sum_of_two_2020(input_numbers: list):
    '''checks which two numbers in the given list add up to 2020
    and then calculates their product'''
    for i in input_numbers:
            for j in input_numbers:
                if int(i) + int(j) == 2020:
                    return int(i) * int(j)


def find_sum_of_three_2020(input_numbers: list):
    '''checks which three numbers in the given list add up to 2020
    and then calculates their product'''
    for i in input_numbers:
            for j in input_numbers:
                for k in input_numbers:
                    if int(i) + int(j) + int(k) == 2020:
                        return int(i) * int(j) * int(k)


if __name__ == "__main__":
    print(f'The answer for the 1st task is: {find_sum_of_two_2020(input_numbers)}')
    print(f'The answer for the 2nd task is: {find_sum_of_three_2020(input_numbers)}')