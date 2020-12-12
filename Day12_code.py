'''This programm is a solution
for day 12 challenges of Advent of Code 2020:
Rain Risk.

Before running this code you should copy your
input data into the clipboard'''

import pyperclip

def get_instructions(data):
    data = data.split('\r\n')
    instructions = []
    for string in data:
        direc = string[0]
        steps = int(string[1:])
        instructions.append((direc, steps))
    return instructions


def guess_move(instr: tuple, start: list, waypoint: list):
    if instr[0] == 'F':
        if start[2] == 0:
            start[1] += instr[1]
        elif start[2] == 90:
            start[0] += instr[1]
        elif start[2] == 180:
            start[1] -= instr[1]
        else:
            start[0] -= instr[1]
    elif instr[0] == 'N':
        start[1] += instr[1]
    elif instr[0] == 'E':
        start[0] += instr[1]
    elif instr[0] == 'S':
        start[1] -= instr[1]
    elif instr[0] == 'W':
        start[0] -= instr[1]
    elif instr[0] == 'R':
        start[2] = (start[2] + instr[1]) % 360
    else:
        start[2] = (start[2] - instr[1]) % 360
    return start


def move_by_waypoint(instr: tuple, start: list, waypoint: list):
    if instr[0] == 'F':
        start[0] += waypoint[0] * instr[1]
        start[1] += waypoint[1] * instr[1]
    elif instr[0] == 'N':
        waypoint[1] += instr[1]
    elif instr[0] == 'E':
        waypoint[0] += instr[1]
    elif instr[0] == 'S':
        waypoint[1] -= instr[1]
    elif instr[0] == 'W':
        waypoint[0] -= instr[1]
    elif instr == ('R', 90) or instr == ('L', 270):
        waypoint[0], waypoint[1] = waypoint[1], - waypoint[0]
    elif instr == ('L', 90) or instr == ('R', 270):
        waypoint[0], waypoint[1] = - waypoint[1], waypoint[0]
    else:
        waypoint[0], waypoint[1] = - waypoint[0], - waypoint[1]
    return start


def navigation(func, instructions, start, waypoint = [10, 1]):
    for instr in instructions:
        func(instr, start, waypoint)
    manhattan_distance = abs(start[0]) + abs(start[1])
    return manhattan_distance

if __name__ == '__main__':
    data = pyperclip.paste()
    instructions = get_instructions(data)
    answer1 = navigation(guess_move, instructions, [0, 0, 90])
    answer2 = navigation(move_by_waypoint, instructions, [0, 0])
    print(answer1, answer2)
    
    



