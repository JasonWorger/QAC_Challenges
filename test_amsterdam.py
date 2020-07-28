import pytest
import amsterdam

def test_amsterdam_test1():
    assert amsterdam.amsterdam("Am I in Amsterdam") == 1

def test_amsterdam_test2():
    assert amsterdam.amsterdam("I am in Amsterdam am I") == 2

def test_amsterdam_test3():
    assert amsterdam.amsterdam("I have been in Amsterdam") == 0