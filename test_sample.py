
# coding: utf-8

# ####### 27/May/2016: 
# ##### ===========
# ** pytest play ground

""" What's the condition to be met to have py.test execute from the command line without any hiccups ?

1. Files should be named as either *_test.py or test_*.py
2. pytest module should be installed (obviously, it's not part of standard library set) including it's
dependencies, like, py, pluggy
3. Single *_test or test_* can include multiple test scenarios ?

"""

import pytest

def test_negation():
    assert False == True

def test_true():
    assert True == True

def test_false():
    assert False == False

def calfunc(intnum):
    return intnum + 51

def test_calcfunc():
    assert calfunc(17) == 34

def test_one():
    testvar = 'hello'
    assert 'hell' in testvar
    
def test_two():
    teststr = 'welcome'
    assert hasattr('go', teststr)
    
if __name__ == "__main__":
    pytest.main()