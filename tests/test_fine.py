
def calculate_fine(days_late):
    if days_late < 0:
        raise ValueError("Days late cannot be negative")
    elif days_late < 5:
        return 0
    elif days_late <= 10:
        return days_late * 20
    elif days_late <= 20:
        return days_late * 50
    else:
        return days_late * 100


def test_no_fine():
    assert calculate_fine(3) == 0


def test_fine_for_6_days():
    assert calculate_fine(6) == 120


def test_fine_for_15_days():
    assert calculate_fine(15) == 750


def test_fine_for_more_than_20_days():
    assert calculate_fine(25) == 2500


def test_negative_days():
    try:
        calculate_fine(-2)
        assert False, "Negative days should be rejected"
    except ValueError:
        pass


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
