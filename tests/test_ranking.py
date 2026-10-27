def rank_students(roster):
    return roster


def test_empty_roster_returns_empty_list():
    roster = []
    assert rank_students(roster) == []


def test_single_student_returns_that_student():
    roster = ["Ali"]
    assert rank_students(roster) == ["Ali"]