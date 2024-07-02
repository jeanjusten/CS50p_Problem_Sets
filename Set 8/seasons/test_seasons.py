import pytest
import seasons
from seasons import get_minutes

def test_get_minutes():
    assert get_minutes("1992-02-10") == "Sixteen million, nine hundred forty-five thousand, nine hundred twenty minutes"

def test_get_minutes_format():
    with pytest.raises(SystemExit):
        assert get_minutes("February 10th, 1992")