import twttr
from twttr import shorten

def test_shorten():
    assert shorten("banana") == "bnn"

def test_shorten_upper():
    assert shorten("bAnanA") == "bnn"

def test_shorten_numbers():
    assert shorten("banana1") == "bnn1"

def test_shorten_characters():
    assert shorten("b.anana") == "b.nn"