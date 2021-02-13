'''This programm is a solution
for day 8 challenges of Advent of Code 2020:
Handheld Halting

Before running this code you should copy your
input data into the clipboard'''

import copy
import pyperclip

data = pyperclip.paste()

def clean_commands(data):
    '''
    Parameters
    ----------
    commands : string
        
    Returns
    -------
    steps : list (of lists)
    '''
    commands = data.split('\r\n')
    steps = []
    for command in commands:
        instruction = command[0:3]
        if command[4] == '+':
            step_num = int(command[5:])
        else:
            step_num = - int(command[5:])
        steps.append([instruction, step_num])
    return steps

def play_game(steps):
    '''
    Follows the game command until the first loop
    Parameters
    ----------
    steps : TYPE
        list of commands - each of them is a list 

    Returns
    -------
    list
        two values - game result and the first step that was not executed
    '''
    game = [0]*len(steps)
    i = 0
    game_sum = 0
    while i < len(game) and game[i] == 0:
        if steps[i][0] == 'nop':
            game[i] = 1
            i += 1
        elif steps[i][0] == 'acc':
            game_sum += steps[i][1]
            game[i] = 1
            i += 1
        else:
            game[i] = 1
            i += steps[i][1]
    return [game_sum, i]

def fix_game(steps):
    '''
    Tries to fix the game step by step until success
    Parameters
    ----------
    steps : list
        initial list of commands - each of them is a list 

    Returns
    -------
    int
        result of the fixed game

    '''
    for i in range(len(steps)):
        if steps[i][0] == 'nop':
            steps_deepcopy = copy.deepcopy(steps)
            steps_deepcopy[i][0] = 'jmp'
            last_step = play_game(steps_deepcopy)[1]
            if last_step >= len(steps):
                return play_game(steps_deepcopy)
        elif steps[i][0] == 'jmp':
            steps_deepcopy = copy.deepcopy(steps)
            steps_deepcopy[i][0] = 'nop'
            last_step = play_game(steps_deepcopy)[1]
            if last_step >= len(steps):
                return play_game(steps_deepcopy)[0]


if __name__ == '__main__':
    steps = clean_commands(data)
    print(play_game(steps)[0])
    print(fix_game(steps))


    
