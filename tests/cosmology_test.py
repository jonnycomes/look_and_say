from look_and_say import *

def test_decay_tree():
    '''Testing the decay_tree method on 22233'''
    cosmo = Cosmology()
    assert cosmo.decay_tree('22233') == {'22233': ['3', '22', '3']}


def test_cosmology_proof(capsys):
    '''
    Testing that the upper bound of 27 days for the age of an exotic 
    element appears in the printout of the proof of the Cosmological Theorem.
    '''
    cosmo = Cosmology()
    cosmo.proof()
    captured = capsys.readouterr()
    assert 'bound of 27 days for the age of an exotic element' in captured.out
