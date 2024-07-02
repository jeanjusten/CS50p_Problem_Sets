import numb3rs
import pytest
from numb3rs import validate

def test_validate_valid():
    assert validate("1.2.3.4") == True
    assert validate("255.255.255.255") == True
    assert validate("10.10.0.1") == True
    assert validate("010.010.00.01") == True

def test_validate_invalid():
    assert validate("1000.0.3.4") == False
    assert validate("1.2..4") == False
    assert validate("275.275.275.275") == False
    assert validate("cat") == False
    assert validate("-1.@.!.%") == False
    assert validate("1.2.3.4.5.6") == False
    assert validate("255.275.1999.10") == False
    assert validate("bird.cat.dog.duck") == False
    assert validate("1.256.1.1") == False

def test_validate_zeroes():
    assert validate("0.0.0.0") == True
    assert validate("000.00.0.00") == True
    assert validate("000.000.000.000") == True