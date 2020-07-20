import pytest
import string_gen

def test_string_gen_islower():
     assert string_gen.string_gen().islower()

def test_string_gen_length():
     assert len(string_gen.string_gen()) == 5

def test_string_gen_istring():
    assert type(string_gen.string_gen()) is str

    