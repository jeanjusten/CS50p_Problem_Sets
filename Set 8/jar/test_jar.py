import pytest
from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(3)
    assert jar.cookies == 3
    assert jar.cookies
    with pytest.raises(ValueError):
        assert jar.deposit(15)

def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    assert jar.withdraw(5) == jar.cookies == 5
    with pytest.raises(ValueError):
        assert jar.withdraw(15)