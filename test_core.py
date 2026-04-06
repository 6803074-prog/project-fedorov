import core

def test_is_even_with_even_number():
    assert core.is_even(4) is True

def test_is_even_with_odd_number():
    assert core.is_even(5) is False
