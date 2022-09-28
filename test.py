
from summation import summation


def test_example():
    assert summation(10) == 45


def test_example2():
    assert summation(11) == 55


def test_example3():
    assert summation(-1) == 0
