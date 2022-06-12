from look_and_say import *

def test_split_Conway_empty():
    '''The empty string does not split'''
    assert split_Conway('') == ['']

def test_split_Conway_methuselum():
    '''Methuselum does not split'''
    assert split_Conway('2233322211n') == ['2233322211n']

def test_split_Conway_multiple_splits1():
    '''Testing the splitting of a string that splits at multiple positions'''
    assert split_Conway('12111322138127') == ['12', '1113', '22', '138', '12', '7']

def test_split_Conway_multiple_splits2():
    '''Testing the splitting of another string that splits at multiple positions'''
    assert split_Conway('132211132122311229') == ['13', '22', '111321', '22', '311', '22', '9']

def test_split_func_factory_declare_split_after_0():
    '''Testing the declare_split_after method after runs of 0's'''
    sff = SplitFuncFactory()
    sff.declare_split_after('0')
    split = sff.get_split()
    assert split('0123400023451234076560034') == ['0', '1234000', '234512340', '765600', '34']

def test_split_func_factory_declare_split_before_0():
    '''Testing the declare_split_before method before runs of 0's'''
    sff = SplitFuncFactory()
    sff.declare_split_before('0')
    split = sff.get_split()
    assert split('01234000234512340765600340') == ['01234', '00023451234', '07656', '0034', '0']


def test_split_func_factory_declare_split_after_multiple():
    '''Testing the declare_split_after method with multiple parameters'''
    sff = SplitFuncFactory()
    sff.declare_split_after('12', '44', '333')
    split = sff.get_split()
    assert split('012114442123400122333123441') == ['012', '11444', '212', '3400122333', '12', '344', '1']


def test_split_func_factory_declare_split_before_multiple():
    '''Testing the declare_split_before method with multiple parameters'''
    sff = SplitFuncFactory()
    sff.declare_split_before('12', '44', '333')
    split = sff.get_split()
    assert split('012114442123400122333123441') == ['0', '1211', '4442', '123400', '122', '333', '123', '441']


def test_split_func_factory_declare_splitting_pairs_multiple():
    '''Testing the declare_splitting_pairs method with multiple parameters'''
    sff = SplitFuncFactory()
    sff.declare_splitting_pairs(('311', '223'), ('0', '1'))
    split = sff.get_split()
    assert split('12311223323112011200011110234234') == ['12311', '2233231120', '112000', '11110234234']
