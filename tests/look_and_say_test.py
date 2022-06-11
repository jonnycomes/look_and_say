from look_and_say import *

def test_say_what_you_see():
    '''Testing the say_what_you_see method for the standard look and say'''
    std = LookAndSay()
    assert std.say_what_you_see('11133222200') == '31234220'

def test_binary_say_what_you_see():
    '''Testing the say_what_you_see method for the standard binary look and say'''
    def say(num):
        return f'{num:b}'
    binary = LookAndSay(say)
    assert binary.say_what_you_see('111100011') == '1001110101'

def test_2_parameter_say_what_you_see():
    '''Testing the say_what_you_see method for a two parameter (stuttering with echo) look and say'''
    def say(num, char):
        return str(num)*2 + char*2
    stutter_echo = LookAndSay(say)
    assert stutter_echo.say_what_you_see('112220') == '221133221100'

