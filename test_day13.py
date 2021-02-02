'''
Test the Day 13 / Part 1 Solution
'''

from Day13_code import clean_buses, find_time

test_data = '''939
7,13,x,x,59,x,31,19'''

def test_type_clean_buses():
    '''
    test output type
    '''
    assert type(clean_buses(test_data)) == list
    
def test_type_find_time():
    '''
    test output type
    '''
    assert type(find_time(test_data)) == tuple
    
def test_find_time():
    '''
    test example input->output
    '''
    result = find_time(test_data)
    assert result[0] * result[1] == 295

