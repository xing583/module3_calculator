import pytest
from app.operations import Operations


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 2, 3),
        (-1, 1, 0),
        (2.5, 0.5, 3.0),
    ],
)
def test_add(a, b, expected):
    assert Operations.add(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (5, 2, 3),
        (0, 3, -3),
        (-2, -2, 0),
    ],
)
def test_subtract(a, b, expected):
    assert Operations.subtract(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (2, 3, 6),
        (-2, 3, -6),
        (0, 10, 0),
    ],
)
def test_multiply(a, b, expected):
    assert Operations.multiply(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (6, 3, 2),
        (5, 2, 2.5),
        (-9, 3, -3),
    ],
)
def test_divide(a, b, expected):
    assert Operations.divide(a, b) == expected


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        Operations.divide(1, 0)
