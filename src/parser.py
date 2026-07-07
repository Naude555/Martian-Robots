from src.robot import Robot


def parse_robot(position, instructions):
    x, y, direction = position.split()

    return Robot(
        x=int(x),
        y=int(y),
        direction=direction,
        instructions=instructions,
    )