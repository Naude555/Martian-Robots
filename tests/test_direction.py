from src.direction import LEFT, RIGHT


def test_turn_left():
    assert LEFT["N"] == "W"
    assert LEFT["E"] == "N"


def test_turn_right():
    assert RIGHT["N"] == "E"
    assert RIGHT["W"] == "N"