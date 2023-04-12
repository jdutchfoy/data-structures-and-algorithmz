# test_is_balanced.py

import pytest
from is_balanced import is_balanced

def test_is_balanced():
    # Happy path
    assert is_balanced('({[]})') == True
    # Unbalanced
    assert is_balanced('({[)})') == False
    # No brackets
    assert is_balanced('hello world') == True
    # Single bracket
    assert is_balanced('(') == False
    # Only opening brackets
    assert is_balanced('({[') == False
    # Only closing brackets
    assert is_balanced(']})') == False