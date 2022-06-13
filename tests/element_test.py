from look_and_say import *

def binary_say(num):
    return "{0:b}".format(num)

binary_ls = LookAndSay(binary_say)
binary_chem = BinaryChemistry(binary_ls)
binary_chem.generate_elements('0')

def negafibnary_say(num):
    assert num < 9
    say = {1:'1', 2:'100', 3:'101', 4:'10010', 5:'10000', 6:'10001', 7:'10100', 8:'10101'}
    return say[num]

negafibnary = LookAndSay(negafibnary_say)
negafibnary_chem = BinaryChemistry(negafibnary)
negafibnary_chem.generate_elements('0')


def test_element_equality():
    '''Testing __eq__ on Element objects'''
    a = [e for e in binary_chem.get_elements() if e.get_string() == '10'][0]
    b = [e for e in binary_chem.get_elements() if e.get_string() == '1110'][0]
    c = [e for e in negafibnary_chem.get_elements() if e.get_string() == '10'][0]
    assert a != '10'
    assert a != 'E1'
    assert a != b
    assert a != c
    assert a == a

def test_printing_element(capsys):
    '''Testing __str__ on Element objects'''
    a, b = negafibnary_chem.get_elements()
    print(a, b)
    captured = capsys.readouterr()
    assert captured.out == 'E1 E2\n'

def test_element_hash():
    '''Testing __hash__ on Element objects'''
    a = [e for e in binary_chem.get_elements() if e.get_string() == '10'][0]
    b = [e for e in binary_chem.get_elements() if e.get_string() == '1110'][0]
    c = [e for e in negafibnary_chem.get_elements() if e.get_string() == '10'][0]
    assert {a, b, c, a} == {a, b, c}
    assert {a, c} != {a}

