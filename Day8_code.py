'''This programm is a solution
for day 8 challenges of Advent of Code 2020:
Handheld Halting.

Before running this code you should copy your
input data into the clipboard'''

import copy

import pyperclip

data = pyperclip.paste()


def make_rule_list(data):
    #print(data[:5])
    rules = data.split('\r\n')
    rule_list = []
    for rule in rules:
        sep = rule.split(' ')
        rule_list.append([sep[0], sep[1], 0])
    return rule_list


def play_game(start_pos, start_score, data):
    rule_list = make_rule_list(data)
    pos = start_pos
    score = start_score
    while pos < len(rule_list) and rule_list[pos][2] != 1:
        
        if rule_list[pos][0] == 'nop':
            #print(pos, score)
            rule_list[pos][2] += 1
            pos += 1
        elif rule_list[pos][0] == 'jmp':
            #print(pos, score)
            rule_list[pos][2] += 1
            if rule_list[pos][1][:1] == '+':
                pos += int(rule_list[pos][1][1:])
            else:
                pos -= int(rule_list[pos][1][1:])
        else:
            #print(pos, score)
            rule_list[pos][2] += 1
            if rule_list[pos][1][:1] == '+':
                score += int(rule_list[pos][1][1:])
                pos += 1
            else:
                score -= int(rule_list[pos][1][1:])
                pos += 1
    if pos >= len(rule_list):
        print(score)
        print('out')
        return ('out', score)
    else:
        #print('loop')
        return ('loop', score)
    
    
def fix_bug(data):
    rule_list = make_rule_list(data)
    print(rule_list[:5])
    for i in range(len(rule_list)):
        new_list = copy.deepcopy(rule_list)
        if new_list[i][0] == 'nop':
            new_list[i][0] = 'jmp'
            print("tryed",i, new_list[i])
            print(play_game(0,0,data))
            if play_game(0,0,data)[0] == 'out':
                print('out')
                return (i, play_game(0,0,new_list)[1])
        elif new_list[i][0] == 'jmp':
            new_list[i][0] = 'nop'
            print("tryed",i, new_list[i])
            print(play_game(0,0,data))
            if play_game(0,0,data)[0] == 'out':
                print('out')
                return (i, play_game(0,0,new_list)[1])
            
def game_two(start_pos, start_score, rule_list):
    pos = start_pos
    score = start_score
    while pos < len(rule_list) and rule_list[pos][2] != 1:
        
        if rule_list[pos][0] == 'nop':
            #print(pos, score)
            rule_list[pos][2] += 1
            pos += 1
        elif rule_list[pos][0] == 'jmp':
            #print(pos, score)
            rule_list[pos][2] += 1
            if rule_list[pos][1][:1] == '+':
                pos += int(rule_list[pos][1][1:])
            else:
                pos -= int(rule_list[pos][1][1:])
        else:
            #print(pos, score)
            rule_list[pos][2] += 1
            if rule_list[pos][1][:1] == '+':
                score += int(rule_list[pos][1][1:])
                pos += 1
            else:
                score -= int(rule_list[pos][1][1:])
                pos += 1
    if pos >= len(rule_list):
        print(score)
        return ('out', score)
    else:
        #print('loop')
        return ('loop', score)
            
if __name__ == '__main__':    
    print(play_game(0, 0, data))
    rule_list = make_rule_list(data)
    for i in range(len(rule_list)):
        new_list = copy.deepcopy(rule_list)
        if new_list[i][0] == 'nop':
            new_list[i][0] = 'jmp'
            #print("tryed",i, new_list[i])
            #print(game_two(0,0,new_list))
            if game_two(0,0,new_list)[0] == 'out':
                break
        elif new_list[i][0] == 'jmp':
            new_list[i][0] = 'nop'
            #print("tryed",i, new_list[i])
            answer = game_two(0,0,new_list)
            if answer[0] == 'out':
                print('ended with', i, answer[1])
                break

