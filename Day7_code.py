'''This is a quick/first approach solution for the task1 of Day7.

Before running this code you should copy your
input data into the clipboard'''

import pyperclip
import re

data = pyperclip.paste()

rules = data.split('\r\n')

outer_bag_re = r'^([a-z].+) bags contain'

final_bags = []
check_bags = [['shiny gold']]
outer_bags = []
stop = False
while stop == False:
    for inner_bag in check_bags:
        #print(inner_bag)
        for rule in rules:
            if inner_bag[0] in rule:
                outer_bag = re.findall(outer_bag_re, rule)
                #print(outer_bag)
                if outer_bag != inner_bag and outer_bag not in final_bags:
                    final_bags.append(outer_bag)
                    outer_bags.append(outer_bag)
    if outer_bags == []:
        stop = True
    check_bags = outer_bags
    outer_bags = []
    
print(len(final_bags))
