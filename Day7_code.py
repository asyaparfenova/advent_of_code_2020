'''This programm is a solution
for day 6 challenges of Advent of Code 2020:
Handy Haversacks.

Before running this code you should copy your
input data into the clipboard'''

import re

import pyperclip

data = pyperclip.paste()
rules = data.split('\r\n')

def calc_outer_bags(rules):
    '''input - list of strings describing colour rules
    for each colour of bags''' 
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
    return len(final_bags)


def calc_inner_bags(rules): 
    '''input - list of strings describing colour rules
    for each colour of bags'''       
    content_re = r'(\d+) ([\w| ]+) bag[s]*'
    check_bags = {'shiny gold':1}
    sum_bags = 0
    while check_bags != {}:
        content_dict = {}
        
        for key in check_bags:
            for string in rules:
                if string[:len(key)] == key:
                    content = re.findall(content_re, string)
                    for item in content:
                        if item[1] not in content_dict.keys():
                            content_dict[item[1]] = int(item[0]) * check_bags[key]
                        else:
                            content_dict[item[1]] += int(item[0]) * check_bags[key]   
                else:
                    pass                   
        for content_key in content_dict:
            sum_bags += content_dict[content_key]
        check_bags = content_dict.copy()
    return sum_bags
    
if __name__ == '__main__':    
    print('Total outer bags:', calc_outer_bags(rules))
    print('Total inner bags:', calc_inner_bags(rules))
