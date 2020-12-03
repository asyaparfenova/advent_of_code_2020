'''This programm calculates the answer
for day 3 challenges of Advent of Code 2020:
    calculating trees (#) pn the symbolic map.

Before running this code you should copy your
input data into the clipboard'''


import re
import pyperclip

data = pyperclip.paste()

def make_map(data):
    line_re = r'[.|#]+'
    input_lines = re.findall(line_re, data)
    dev = len(input_lines) // len(input_lines[0])
    map = []
    for line in input_lines:
        map.append(line * 3 * (dev + 1))
    return map

def count_trees(map):
    x = 0
    trees = 0
    for row in map:
        if row[x] == '#':
            trees += 1
        x += 3
    return trees

if __name__ == "__main__":
    forest = make_map(data)
    trees = count_trees(forest)
    print('You incountered', trees, 'trees :/')