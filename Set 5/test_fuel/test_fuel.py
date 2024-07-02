import fuel
import pytest
from fuel import convert, gauge

def test_convert():
    assert convert("3/4") == 75
    assert convert("4/4") == 100
    assert convert("1/4") == 25
    assert convert("10/20") == 50

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        assert convert("2/0")

def test_value():
    with pytest.raises(ValueError):
        assert convert("a/b")

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"
