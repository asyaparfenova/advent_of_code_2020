'''This programm is a solution
for day 10 challenges of Advent of Code 2020:
Adapter Array.

Before running this code you should copy your
input data into the clipboard'''

import pyperclip
import copy


def get_map(data):
    seat_map = data.split('\r\n')
    for r in range(len(seat_map)):
        seat_map[r] = list(seat_map[r])
    return seat_map
    

def check_around(smap, r, s):
    j = '#' 
    if r == 0 and s == 0:
        app = [smap[0][1], smap[1][1],smap[1][0]].count(j)
            
    elif r == 0 and s == len(smap[r]) - 1:
        app = [smap[0][s-1], smap[1][s-1], smap[1][s]].count(j)

    elif r == 0 and s < len(smap[r]) - 1 and s > 0:
        app = [smap[r][s+1],smap[r][s-1],smap[r+1][s+1], smap[r+1][s], smap[r+1][s-1]].count(j)

    elif r > 0 and r < len(smap) - 1 and s == 0:
        app = [smap[r-1][s],smap[r-1][s+1],smap[r][s+1], smap[r+1][s], smap[r+1][s+1]].count(j)

    elif r > 0 and r < len(smap) - 1 and s == len(smap[r]) - 1:
        app = [smap[r-1][s],smap[r-1][s-1],smap[r][s-1], smap[r+1][s], smap[r+1][s-1]].count(j)

    elif r == len(smap) - 1 and s == len(smap[r]) - 1:
        app = [smap[r-1][s],smap[r-1][s-1],smap[r][s-1]].count(j)
     
    elif r == len(smap) - 1 and s == 0:
        app = [smap[r-1][s],smap[r-1][s+1],smap[r][s+1]].count(j)
      
    elif r == len(smap) - 1 and s > 0 and s < len(smap[r]) - 1:
        app = [smap[r-1][s],smap[r-1][s+1],smap[r-1][s-1], smap[r][s-1], smap[r][s+1]].count(j)
         
    else:
        app =  [smap[r-1][s],smap[r-1][s+1],smap[r-1][s-1], smap[r][s-1], smap[r][s+1],smap[r+1][s],smap[r+1][s+1],smap[r+1][s-1]].count(j)
        
    return app


def tolerant_check(sm: list, r, s):
    cal = 0
    step = 1
    stop = False
    while stop == False and r - step >= 0:
        if sm[r-step][s] == 'L':
            stop = True
        elif sm[r-step][s] == '#':
            cal += 1
            stop = True
        else:
            step += 1
    stop = False
    step = 1
    while stop == False and r - step >= 0 and s + step < len(sm[r]):
        if sm[r-step][s + step] == 'L':
            stop = True
        elif sm[r-step][s + step] == '#':
            cal += 1
            stop = True
        else:
            step += 1
    stop = False
    step = 1
    while stop == False and s + step < len(sm[r]):
        if sm[r][s + step] == 'L':
            stop = True
        elif sm[r][s + step] == '#':
            cal += 1
            stop = True
        else:
            step += 1
    stop = False
    step = 1
    while stop == False and r + step < len(sm) and s + step < len(sm[r]):
        if sm[r + step][s + step] == 'L':
            stop = True
        elif sm[r + step][s + step] == '#':
            cal += 1
            stop = True
        else:
            step += 1
    stop = False
    step = 1
    while stop == False and r + step < len(sm):
        if sm[r + step][s] == 'L':
            stop = True
        elif sm[r + step][s] == '#':
            cal += 1
            stop = True
        else:
            step += 1
    stop = False
    step = 1
    while stop == False and r + step < len(sm) and s - step >= 0:
        if sm[r + step][s - step] == 'L':
            stop = True
        elif sm[r + step][s - step] == '#':
            cal += 1
            stop = True
        else:
            step += 1
    stop = False
    step = 1
    while stop == False and s - step >= 0:
        if sm[r][s - step] == 'L':
            stop = True
        elif sm[r][s - step] == '#':
            cal += 1
            stop = True
        else:
            step += 1
    stop = False
    step = 1
    while stop == False and s - step >= 0 and r - step >= 0:
        if sm[r - step][s - step] == 'L':
            stop = True
        elif sm[r - step][s - step] == '#':
            cal += 1
            stop = True
        else:
            step += 1
    return cal


def passengers_wave(func, seat_map, tolerated_max):
    while True:
        changed_map = copy.deepcopy(seat_map)
        for r in range(len(seat_map)):
            for s in range(len(seat_map[r])):
                if seat_map[r][s] == 'L':
                    if func(seat_map, r, s) == 0:
                        changed_map[r][s] = '#'
                elif seat_map[r][s] == '#':
                    if func(seat_map, r, s) >= tolerated_max:
                        changed_map[r][s] = 'L'
        if seat_map == changed_map:
            break
        else:
            seat_map = changed_map
    return changed_map


def count_occup_seats(map):
    cal = 0
    for r in range(len(map)):
        for s in range(len(map[r])):
            if map[r][s] == '#':
                cal += 1
    return cal


if __name__ == '__main__':
    data = pyperclip.paste()
    seat_map = get_map(data)
    first_map = passengers_wave(check_around, seat_map, 4)
    second_map = passengers_wave(tolerant_check, seat_map, 5)
    print(count_occup_seats(first_map), count_occup_seats(second_map))