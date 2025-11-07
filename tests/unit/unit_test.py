import pytest
from ...src.pricing import parse_price

def test_valid_parse_price():
    parsed_price = parse_price("$1,234.5")
    assert parsed_price == 1234.5