import pytest
from code_challenges.stack_queue_brackets import multi_bracket_validation

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
@pytest.mark.skip("TODO")
def test_validates_two_square_brackets():
    actual = multi_bracket_validation("[]")
    expected = True
    assert actual == expected


@pytest.mark.skip("TODO")
def test_fails_two_square_brackets_flipped():
    actual = multi_bracket_validation("][")
    expected = False
    assert actual == expected


@pytest.mark.skip("TODO")
def test_validates_two_braces():
    actual = multi_bracket_validation("{}")
    expected = True
    assert actual == expected


@pytest.mark.skip("TODO")
def test_fails_two_braces_flipped():
    actual = multi_bracket_validation("}{")
    expected = False
    assert actual == expected


@pytest.mark.skip("TODO")
def test_validates_two_parentheses():
    actual = multi_bracket_validation("()")
    expected = True
    assert actual == expected


@pytest.mark.skip("TODO")
def test_fails_two_parentheses_flipped():
    actual = multi_bracket_validation(")(")
    expected = False
    assert actual == expected


@pytest.mark.skip("TODO")
def test_multi():
    actual = multi_bracket_validation("{}(){}")
    expected = True
    assert actual == expected


@pytest.mark.skip("TODO")
def test_nested():
    actual = multi_bracket_validation("{([])}")
    expected = True
    assert actual == expected


@pytest.mark.skip("TODO")
def test_mismatched():
    actual = multi_bracket_validation("[}")
    expected = False
    assert actual == expected

