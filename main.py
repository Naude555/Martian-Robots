import sys


def parse_robot(position, instructions):
    x, y, direction = position.split()

    return {
        "x": int(x),
        "y": int(y),
        "direction": direction,
        "instructions": instructions,
    }

def main():
    lines = [line.strip() for line in sys.stdin if line.strip()]

    max_x, max_y = map(int, lines[0].split())

    robots = []

    for i in range(1, len(lines), 2):
        robots.append(parse_robot(lines[i], lines[i + 1]))

    print(f"World: ({max_x}, {max_y})")
    print()

    for robot in robots:
        print(robot)


if __name__ == "__main__":
    main()