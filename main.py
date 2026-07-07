import sys

from src.robot import Robot
from src.simulator import simulate
from src.world import World


def parse_robot(position, instructions):
    x, y, direction = position.split()

    return Robot(
        x=int(x),
        y=int(y),
        direction=direction,
        instructions=instructions,
    )

def main():
    lines = [line.strip() for line in sys.stdin if line.strip()]

    world = World(max_x=int(lines[0].split()[0]), max_y=int(lines[0].split()[1]), scents=set())

    robots = []

    for i in range(1, len(lines), 2):
        robots.append(parse_robot(lines[i], lines[i + 1]))

    print(f"World: ({world.max_x}, {world.max_y})")
    print()

    for robot in robots:
        simulate(robot, world.max_x, world.max_y, world.scents)
        print(f"{robot.x} {robot.y} {robot.direction}{' LOST' if robot.lost else ''}")


if __name__ == "__main__":
    main()