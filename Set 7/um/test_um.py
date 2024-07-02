import pytest
import um
from um import count

def test_count():
    assert count("Did you choose this album?") == 0
    assert count("Hello, um... um.. what?") == 2
    assert count("Um, hello there!") == 1
    assert count("I wasn't, um, doing anything") == 1

def test_count_2():
    assert count("Hey... um, it was you, um that did it?") == 2
    assert count("My photo album is the one with um, blue cover") == 1
    assert count("Umm... what are you doing here? Um.") == 1

def test_count_3():
    assert count("Um, hello there UM....") == 2
    assert count("UM, STOP YELLING AT ME!") == 1