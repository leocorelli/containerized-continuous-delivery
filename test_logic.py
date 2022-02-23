from logic import squares


def test_squares():
    assert [1, 4, 9, 16, 25, 36] == squares(6)
