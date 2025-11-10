from hello import add
from hello import multiply

def test_add():
    assert add(1, 2) == 3


def test_multiply():
    assert multiply(3, 2) == 6