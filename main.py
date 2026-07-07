import sys

from robot import Robot

# How do we turn
LEFT = {
    "N": "W",
    "W": "S",
    "S": "E",
    "E": "N",
}

RIGHT = {
    "N": "E",
    "E": "S",
    "S": "W",
    "W": "N",
}

# How do we move 
MOVE = {
    "N": (0, 1),
    "E": (1, 0),
    "S": (0, -1),
    "W": (-1, 0),
}

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

        instructions = robot.instructions
        lost = robot.lost

        for instruction in instructions:
            if instruction == "L":
                robot.direction = LEFT[robot.direction]
            elif instruction == "R":
                robot.direction = RIGHT[robot.direction]
            elif instruction == "F":
                dx, dy = MOVE[robot.direction]
                next_x = robot.x + dx
                next_y = robot.y + dy

                if 0 <= next_x <= max_x and 0 <= next_y <= max_y:
                    robot.x, robot.y = next_x, next_y
                else:
                    scent = (robot.x, robot.y, robot.direction)
                    if scent in scents:
                        continue

                    scents.add(scent)
                    robot.lost = True
                    break
        print(f"{robot.x} {robot.y} {robot.direction}{' LOST' if robot.lost else ''}")


if __name__ == "__main__":
    main()