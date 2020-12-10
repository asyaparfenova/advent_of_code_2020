'''This programm is a solution
for day 10 challenges of Advent of Code 2020:
Adapter Array.

Before running this code you should copy your
input data into the clipboard'''

import pyperclip
import pandas as pd


def to_intlist(data):
    '''
    makes an ordered list of all adapters, incl. outlet and device
    '''
    joltage_strings = data.split('\r\n')
    joltage_list = list(map(int,joltage_strings))
    joltage_list.append(max(joltage_list) + 3)
    joltage_list.append(0)
    joltage_list.sort()
    return joltage_list


def multiply_different_adapters(joltage_list):
    '''
    calculates a product of counts of steps of 3 and counts of steps of 1
    '''
    df = pd.DataFrame({'joltage':joltage_list})
    df['diff'] = df['joltage'].diff()
    mult = int(df.groupby(['diff']).count().cumprod().max())
    return mult


def adapters_combinations(joltage_list):
    '''
    counts all possible adaptors combinations
    '''    
    sublist_len = 1
    possibilities = 1
    multipliers = {1:1, 2:1, 3:2, 4:4, 5:7}
    for i in range(len(joltage_list) - 1):
        if joltage_list[i+1] - joltage_list[i] == 1:
            sublist_len += 1
        else:
            possibilities *= multipliers[sublist_len]
            sublist_len = 1
    return possibilities


if __name__ == '__main__':
    data = pyperclip.paste()
    joltage_list = to_intlist(data)
    print(multiply_different_adapters(joltage_list))
    print(adapters_combinations(joltage_list))
