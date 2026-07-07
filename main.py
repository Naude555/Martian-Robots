import sys

from src.simulator import simulate
from src.world import World
from src.parser import parse_robot


def main():
    lines = [line.strip() for line in sys.stdin if line.strip()]

    world = World(max_x=int(lines[0].split()[0]), max_y=int(lines[0].split()[1]))

    robots = []

    for i in range(1, len(lines), 2):
        robots.append(parse_robot(lines[i], lines[i + 1]))

    print(f"World: ({world.max_x}, {world.max_y})")
    print()

    for robot in robots:
        simulate(robot, world)
        print(f"{robot.x} {robot.y} {robot.direction}{' LOST' if robot.lost else ''}")


if __name__ == "__main__":
    main()