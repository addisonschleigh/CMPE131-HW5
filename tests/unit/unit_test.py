import pytest

from src.pricing import parse_price

@pytest.mark.parametrize("input, expected", [
    ("$1,234.5", 1234.5),
    ("12.5", 12.5),
    ("$0.99", 0.99)
])
def test_valid_parse_price(input, expected):
    assert parse_price(input) == expected

@pytest.mark.parametrize("input", [
    (""),
    ("abc")
])
def test_invalid_parse_price(input):
    with pytest.raises(ValueError):
        parse_price(input)
