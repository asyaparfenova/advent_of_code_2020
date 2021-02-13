'''This programm is a solution
for day 5 challenges of Advent of Code 2020:
    finding a highest number seat and a missing seat.

Before running this code you should copy your
input data into the clipboard'''

import pyperclip

data = pyperclip.paste()

boardingpasses = data.split('\r\n') 

def get_row(boardingpass):
    '''calculates the number of row from boarding pass code'''    
    search_rows = list(range(0,128))
    for L in boardingpass[:-3]:
        if L == 'F':
            search_rows = search_rows[0:len(search_rows)//2]
        else:
            search_rows = search_rows[len(search_rows)//2:]
    return int(search_rows[0])

def get_column(boardingpass):
    '''calculates the number of column from boarding pass code'''    
    search_columns = list(range(0,8))
    for L in boardingpass[-3:]:
        if L == 'R':
            search_columns = search_columns[len(search_columns)//2:]
        else:
            search_columns = search_columns[0:len(search_columns)//2]
    return int(search_columns[0])

def get_seat(row, column):
    '''calculates the number of seat from row and column numbers'''
    return row * 8 + column

def get_all_seats(boardingpasses):
    '''creates a list of all seats all from boarding pass codes'''
    all_seats = []
    for b in boardingpasses:
        row = get_row(b)
        column = get_column(b)
        seat = get_seat(row, column)
        all_seats.append(seat)
    return(all_seats)

def find_missing_seat(seats):
    '''finds a non-occupied seat from a list of all seats'''
    total_seats = [x for x in range(seats[0], seats[-1] + 1)]
    seats = set(seats)
    missing_seat = (list(seats ^ set(total_seats)))
    return missing_seat


if __name__ == "__main__":
    seats = get_all_seats(boardingpasses)
    print('Highest seat number is', max(seats))
    seats.sort()
    my_seat = find_missing_seat(seats)
    print('Your seat number is', my_seat[0])
    



