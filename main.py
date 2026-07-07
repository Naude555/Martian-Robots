import sys

from robot import Robot
from simulator import simulate


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

    max_x, max_y = map(int, lines[0].split())

    scents = set()

    robots = []

    for i in range(1, len(lines), 2):
        robots.append(parse_robot(lines[i], lines[i + 1]))

    print(f"World: ({max_x}, {max_y})")
    print()

    for robot in robots:
        simulate(robot, max_x, max_y, scents)
        print(f"{robot.x} {robot.y} {robot.direction}{' LOST' if robot.lost else ''}")


if __name__ == "__main__":
    main()