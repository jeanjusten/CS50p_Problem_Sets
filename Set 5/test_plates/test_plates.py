import plates
from plates import is_valid

def test_valid1():
    assert is_valid("A") == False
    assert is_valid("aaaaaaaaaa") == False

def test_valid2():
    assert is_valid("AA") == True
    assert is_valid("11") == False
    assert is_valid("A1AA") == False

def test_valid3():
    assert is_valid("AA.!11") == False
    assert is_valid("AAAA10") == True
    assert is_valid("AA10AA") == False

def test_valid4():
    assert is_valid("00") == False
    assert is_valid("1A") == False
    assert is_valid("AA01") == False
