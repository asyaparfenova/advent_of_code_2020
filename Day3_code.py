'''This programm calculates the answer
for day 3 challenges of Advent of Code 2020:
    calculating trees (#) pn the symbolic map.

Before running this code you should copy your
input data into the clipboard'''


import re
import pyperclip

data = pyperclip.paste()
steps_set = [(1,1), (3,1), (5,1), (7,1), (1,2)]

def get_listed_map(data: str):
    '''breaks the input into list of lines'''
    line_re = r'[.|#]+'
    listed_map = re.findall(line_re, data)
    return listed_map

def count_trees(map: str, steps: tuple):
    '''counts encountered trees on given map with given steps pattern (x,y)'''
    x = 0
    trees = 0
    for row in map[::steps[1]]:
        if row[x] == '#':
            trees += 1
        x = (x + steps[0]) % len(row)
    return trees

if __name__ == "__main__":
    
    steps_product = 1
    
    for steps in steps_set:
        forest = get_listed_map(data)
        trees = count_trees(forest, steps)
        
        steps_product *= trees
        
        print(f'Following a slope of right {steps[0]} and down {steps[1]}, you will encounter {trees} trees')
    print(f'/nAll trees multiplied are {steps_product}')
        