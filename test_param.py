import yaml
import pytest


def add_function(a, b):
    return a + +b


@pytest.mark.parametrize("a,b,expected",

                         )
def test_add(a, b, expected):
    assert add_function(a, b) == expected
