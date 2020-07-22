import pytest
import sequence

def test_should_sort_sentence():
    assert sequence.sorted_list("This is a sentence is a") == "a is sentence This"
