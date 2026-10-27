
import pytest


def calculate_fine(days_late):
    if days_late < 0:
        raise ValueError("Days late cannot be negative")
    elif days_late <= 5:
        return 0
    elif days_late <= 10:
        return days_late * 20
    elif days_late <= 20:
        return days_late * 50
    else:
        return days_late * 100


# Basic unit tests
def test_no_fine():
    assert calculate_fine(3) == 0


def test_fine_for_6_days():
    assert calculate_fine(6) == 120


def test_fine_for_15_days():
    assert calculate_fine(15) == 750


def test_fine_for_more_than_20_days():
    assert calculate_fine(25) == 2500


# Test invalid input
def test_negative_days():
    with pytest.raises(ValueError):
        calculate_fine(-2)


# Individual boundary tests
def test_boundary_5_days():
    assert calculate_fine(5) == 0


def test_boundary_6_days():
    assert calculate_fine(6) == 120


def test_boundary_10_days():
    assert calculate_fine(10) == 200


def test_boundary_11_days():
    assert calculate_fine(11) == 550


def test_boundary_20_days():
    assert calculate_fine(20) == 1000


def test_boundary_21_days():
    assert calculate_fine(21) == 2100


# Parameterized Boundary Value Analysis tests
@pytest.mark.parametrize("days, expected", [
    (4, 0),
    (5, 0),
    (6, 120),
    (9, 180),
    (10, 200),
    (11, 550),
    (19, 950),
    (20, 1000),
    (21, 2100),
    (0, 0),
    (1, 0),
])
def test_fine_boundaries(days, expected):
    assert calculate_fine(days) == expected


# Fixture: reusable test data
@pytest.fixture
def normal_days():
    return [3, 6, 10]


def test_fines_using_fixture(normal_days):
    assert calculate_fine(normal_days[0]) == 0
    assert calculate_fine(normal_days[1]) == 120
    assert calculate_fine(normal_days[2]) == 200


# Exception testing with pytest
def test_negative_days_with_pytest():
    with pytest.raises(ValueError):
        calculate_fine(-1)
