from look_and_say import *

##### Testing the standard decimal LookAndSay ######
decimal = LookAndSay()

def test_say_what_you_see():
    '''Testing the say_what_you_see method for the standard look and say'''
    assert decimal.say_what_you_see('11133222200') == '31234220'

def test_decimal_sequence():
    '''Testing the decimal say what you see sequence'''
    decimal.generate_sequence(seed='1', terms=6)
    seq = decimal.get_sequence()
    assert seq == ['1', '11', '21', '1211', '111221', '312211']
    assert decimal.get_length_ratios() == [2, 1, 2, 1.5, 1]
    assert decimal.get_last_length_ratio() == 1


##### Testing the standard binary LookAndSay ######
def binary_say(num):
    return f'{num:b}'
binary = LookAndSay(binary_say)

def test_binary_say_what_you_see():
    '''Testing the say_what_you_see method for the standard binary look and say'''
    assert binary.say_what_you_see('111100011') == '1001110101'

def test_binary_sequence():
    '''Testing the binary say what you see sequence'''
    binary.generate_sequence(seed='1', terms=5)
    seq = binary.get_sequence()
    assert seq == ['1', '11', '101', '111011', '11110101']
    assert binary.get_length_ratios()[:-1] == [2, 1.5, 2]
    assert round(binary.get_last_length_ratio(),3) == 1.333


##### Testing a LookAndSay object from a 2 parameter say function (triple stutter with echo) ######
def stutter_echo_say(num, char):
    return str(num)*3 + char*2
stutter_echo = LookAndSay(stutter_echo_say)

def test_2_parameter_say_what_you_see():
    '''Testing the say_what_you_see method for a two parameter (stuttering with echo) say function'''
    assert stutter_echo.say_what_you_see('112220') == '222113332211100'

def test_2_parameter_say_sequence():
    '''Testing q 2 parameter say what you see sequence'''
    stutter_echo.generate_sequence(seed='2', terms=4)
    seq = stutter_echo.get_sequence()
    assert seq == ['2', '11122', '3331122222', '333332221155522']
    assert stutter_echo.get_length_ratios() == [5, 2, 1.5]
    assert stutter_echo.get_last_length_ratio() == 1.5


