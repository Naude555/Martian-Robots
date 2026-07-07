from src.direction import LEFT, RIGHT, MOVE
from src.robot import Robot
from src.world import World


def simulate(robot: Robot, world: World) -> None:
    for instruction in robot.instructions:
        if instruction == "L":
            robot.direction = LEFT[robot.direction]
        elif instruction == "R":
            robot.direction = RIGHT[robot.direction]
        elif instruction == "F":
            dx, dy = MOVE[robot.direction]
            next_x = robot.x + dx
            next_y = robot.y + dy

            if world.contains(next_x, next_y):
                robot.x, robot.y = next_x, next_y
            else:
                if world.has_scent(robot.x, robot.y, robot.direction):
                    continue

                world.add_scent(robot.x, robot.y, robot.direction)
                robot.lost = True
                break
