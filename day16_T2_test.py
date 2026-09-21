import pytest
from day16_T2 import clean_with_functional, clean_with_comprehension, is_non_blank, format_string

@pytest.mark.parametrize("lists", [[], ["  ali", "", "REZA", "   ", "python"], ["ali    ", "   rEZA", "pYthon\t"]])
def test_clean_with_functional_and_comprehensional(lists):
    l1 = clean_with_comprehension(lists)
    l2 = clean_with_functional(lists)
    assert l2 == l1

def test_is_non_blank():
    assert is_non_blank(" ali") == True
    assert is_non_blank("") == False
    assert is_non_blank("       ") == False

def test_format_string():
    assert format_string("  ali") == "Ali"
    assert format_string("reZA      ") == "Reza"