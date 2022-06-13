from look_and_say import *

def test_decay_tree():
    '''Testing the decay_tree method on 22233'''
    cosmo = Cosmology()
    assert cosmo.decay_tree('22233') == {'22233': ['3', '22', '3']}

def test_decay_tree_transuranic():
    '''Testing the decay_tree method on 5'''
    cosmo = Cosmology(digits='123456789')
    assert cosmo.decay_tree('5') == {'5': [{'15': [{'1115': [{'3115': [{'132115': [{'1113122115': [{'311311222115': ['1321132', {'1322115': [{'1113222115': [{'3113322115': ['132', {'123222115': [{'111213322115': [{'31121123222115': [{'132112211213322115': [{'111312212221121123222115': [{'3113112211322112211213322115': [{'1321132122211322212221121123222115': [{'111312211312113221133211322112211213322115': ['31131122211311122113222', '12', '312211322212221121123222115']}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}


def test_cosmology_proof(capsys):
    '''
    Testing that the upper bound of 27 days for the age of an exotic 
    element appears in the printout of the proof of the Cosmological Theorem.
    '''
    cosmo = Cosmology()
    cosmo.proof()
    captured = capsys.readouterr()
    assert 'bound of 27 days for the age of an exotic element' in captured.out


