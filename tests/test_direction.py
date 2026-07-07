from src.direction import LEFT, RIGHT


def test_turn_left():
    assert LEFT["N"] == "W"
    assert LEFT["E"] == "N"
    assert LEFT["S"] == "E"
    assert LEFT["W"] == "S"


def test_turn_right():
    assert RIGHT["N"] == "E"
    assert RIGHT["W"] == "N"
    assert RIGHT["S"] == "W"
    assert RIGHT["E"] == "S"