from look_and_say import *

def test_split_Conway_empty():
    '''The empty string does not split'''
    assert split_Conway('') == ['']

def test_split_Conway_methuselum():
    '''Methuselum does not split'''
    assert split_Conway('2233322211n') == ['2233322211n']

def test_split_Conway_multiple_splits():
    '''Testing the splitting of a string that splits at multiple positions'''
    assert split_Conway('1211132213') == ['12', '1113', '22', '13']