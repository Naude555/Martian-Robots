from src.direction import LEFT, RIGHT, MOVE

def simulate(robot, max_x,max_y, scents):
    for instruction in robot.instructions:
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