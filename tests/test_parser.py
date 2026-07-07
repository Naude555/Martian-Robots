from src.parser import parse_robot


def test_parse_robot():
    robot = parse_robot(
        "1 2 N",
        "RFLFF"
    )

    assert robot.x == 1
    assert robot.y == 2
    assert robot.direction == "N"
    assert robot.instructions == "RFLFF"
    assert robot.lost is False