'''This programm is a solution
for day 13/Part 1 challenge of Advent of Code 2020:
Shuttle Search.

Before running this code you should copy your
input data into the clipboard'''

import pyperclip

data = pyperclip.paste()


def clean_buses(data):
    '''
    Extracts the clean sorted list of Bus IDs as integers
    Parameters
    ----------
    data : string
        task input

    Returns
    -------
    buslist : list
    '''
    buses = data.split('\n')[1]
    buses = buses.split(',')
    buslist = []
    for bus in buses:
        if bus != 'x':
            buslist.append(int(bus))
    buslist.sort()
    return buslist

def find_time(data):
    '''
    Finds the shortest waiting time for the next bus and bus's ID'

    Parameters
    ----------
    data : string
    task inpurt

    Returns
    -------
    bus : int
    (Bus ID)
    waiting_time : int
    '''
    ts = int(data.split('\n')[0])
    buses = clean_buses(data)
    waiting_time = 0
    while True:
        for bus in buses:
            if (ts + waiting_time) % bus == 0:
                return bus, waiting_time
        waiting_time += 1


if __name__ == '__main__':
    bus, waiting_time = find_time(data)              
    print(bus*waiting_time)