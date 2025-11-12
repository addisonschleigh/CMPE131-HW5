import pytest

from src.pricing import parse_price, format_currency, apply_discount, add_tax, bulk_total

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

def test_format_currency():
    assert format_currency(23.145) == "$23.14"

@pytest.mark.parametrize("price, percent, expected", [
    (10,0,10),
    (20,0.95,1)
])
def test_valid_apply_discount(price, percent, expected):
    assert apply_discount(price,percent) == expected

def test_invalid_apply_discount():
    with pytest.raises(ValueError):
        apply_discount(10,-0.1)

def test_default_add_tax():
    assert add_tax(10) == 10.700000000000001 # add_tax calculated weirdly with default

def test_custom_add_tax():
    assert add_tax(15, 0.1) == 16.5

def test_invalid_add_tax():
    with pytest.raises(ValueError):
        add_tax(20, -0.1)

def test_bulk_total():
    list = [3.99,2.99,4.99]
    assert bulk_total(list) == 12.807900000000002 # add_tax calculated weirdly with default