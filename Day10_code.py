'''This programm is a solution
for day 10 challenges of Advent of Code 2020:
Adapter Array.

Before running this code you should copy your
input data into the clipboard'''

import pyperclip
import pandas as pd


def to_intlist(data):
    joltage_strings = data.split('\r\n')
    joltage_list = list(map(int,joltage_strings))
    joltage_list.append(max(joltage_list) + 3)
    joltage_list.append(0)
    return joltage_list

def check_adapters(joltage_list):
    df = pd.DataFrame({'joltage':joltage_list})
    df.sort_values(by=['joltage'], inplace = True)
    df['diff'] = df['joltage'].diff()
    diffs = df.groupby(['diff']).count().shape[0]
    mult = int(df.groupby(['diff']).count().cumprod().max())
    return (diffs, mult)

def mult_diffs_count(adapters_tuple):
    return adapters_tuple[1]

def validate_adapters_list(joltage_list):
    adapters_tuple = check_adapters(joltage_list)
    if adapters_tuple[0] == 2:
        return True

if __name__ == '__main__':
    data = pyperclip.paste()
    joltage_list = to_intlist(data)
    adapters_tuple = check_adapters(joltage_list)
    print('Answer for the task 1:', mult_diffs_count(adapters_tuple))
    print(validate_adapters_list(joltage_list))

