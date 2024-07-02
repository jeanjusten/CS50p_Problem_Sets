import pytest
import working
from working import convert

def test_convert_correct():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("01 AM to 5 PM") == "01:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_convert_correct_minutes():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"

def test_convert_value_error():
    with pytest.raises(ValueError):
        assert convert("9 AM - 5 PM")

def test_convert_value_error_2():
    with pytest.raises(ValueError):
        assert convert("7:98 AM to 10 PM")