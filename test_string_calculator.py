import pytest 

from string_calculator import StringCalculator

@pytest.fixture
def calculator():
    return StringCalculator()

def test_empty_string_returns_zero(calculator):
    assert calculator.add("  ") == 0

def test_single_number_returns_value(calculator):
    assert calculator.add("1") == 1

def test_two_or_more_numbers_return_sum(calculator):
    assert calculator.add("1,2,3,4") == 10