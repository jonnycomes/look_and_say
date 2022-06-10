from look_and_say import *

def test_say_what_you_see():
    '''Testing the say_what_you_see method for the standard look and say'''
    ls = LookAndSay()
    assert ls.say_what_you_see('11133222200') == '31234220'