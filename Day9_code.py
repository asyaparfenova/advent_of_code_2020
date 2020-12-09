'''This programm is a solution
for day 9 challenges of Advent of Code 2020:
Encoding Error.

Before running this code you should copy your
input data into the clipboard'''

import pyperclip

data = pyperclip.paste()
numbers = data.split('\r\n')


def check_sum(to_check, check_list):
    '''checks if any two numbers in the given list add up to 'to_check'
    number and ruterns positive number if yes'''
    bingo = 0
    for i in check_list:
            for j in check_list:
                if int(i) + int(j) == int(to_check) and i != j:
                    bingo += 1
                else:
                    pass
    return bingo


def find_weakness(length, numbers):
    '''finds the first number in the list where
    the previous _length_ numbers to dot pass check_sum'''
    for i in range(length, len(numbers)-1):
        to_check = numbers[i]
        check_list = numbers[i-length: i]
        if check_sum(to_check, check_list) >= 1:
            pass
        else:
            return int(to_check)


def encryption_weakness(numbers, weakness):
    '''the contigious set of numbers that adds up to weakness
    and calculates the sum of min and max of these numbers'''
    for i in range(len(numbers)):
        check_sum = 0
        contiset = []
        j=i
        while check_sum < weakness:
            check_sum += int(numbers[j])
            contiset.append(int(numbers[j]))
            if check_sum == weakness:
                return min(contiset) + max(contiset)
            j += 1


if __name__ == '__main__':  
    weakness = find_weakness(25, numbers)
    print(weakness)
    print(encryption_weakness(numbers, weakness))