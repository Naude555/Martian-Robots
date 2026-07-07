from src.robot import Robot
from src.simulator import simulate
from src.world import World


def test_simulate_moves_robot_within_world():
    world = World(max_x=5, max_y=3)
    robot = Robot(x=1, y=1, direction="E", instructions="RFRFRFRF")

    simulate(robot, world)

    assert robot.x == 1
    assert robot.y == 1
    assert robot.direction == "E"
    assert robot.lost is False
    assert world.scents == set()


def test_simulate_marks_lost_robot_and_adds_scent():
    world = World(max_x=5, max_y=3)
    robot = Robot(x=3, y=2, direction="N", instructions="FRRFLLFFRRFLL")

    simulate(robot, world)

    assert robot.x == 3
    assert robot.y == 3
    assert robot.direction == "N"
    assert robot.lost is True
    assert world.scents == {(3, 3, "N")}


def test_simulate_uses_world_scent_to_ignore_losing_move():
    world = World(max_x=5, max_y=3, scents={(3, 3, "N")})
    robot = Robot(x=3, y=3, direction="N", instructions="F")

    simulate(robot, world)

    assert robot.x == 3
    assert robot.y == 3
    assert robot.direction == "N"
    assert robot.lost is False
    assert world.scents == {(3, 3, "N")}
