from dataclasses import dataclass

@dataclass
class Robot:
    i: tuple
    p: tuple
    v: tuple


def tuple_add(a, b):
    val = (a[0] + b[0], a[1] + b[1])
    return val


with open("C:\\Users\\perki\\Documents\\GitHub\\advent-of-code\\2024\\14\\Input\\input.txt", "r") as file:
    robots = []
    
    for line in file:
        line = line.rstrip("\n")
        data = line.replace("p=","").replace("v=", "").split(" ")
        position = data[0].split(",")
        position = (int(position[0]), int(position[1]))
        velocity = data[1].split(",")
        velocity = (int(velocity[0]), int(velocity[1]))
        robots.append(Robot(position, position, velocity))

    
    max_x = 101
    max_y = 103

    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0

    for robot in robots:
        for i in range(100):
            robot.p = tuple_add(robot.p, robot.v)
        
        robot.p = (robot.p[0] % max_x, robot.p[1])
        robot.p = (robot.p[0], robot.p[1] % max_y)

        if robot.p[0] == int(max_x/2) or robot.p[1] == int(max_y/2):
            print("skipping " + str(robot.p))
            continue

        if robot.p[0] > (max_x/2):
            if robot.p[1] > (max_y/2):
                print("q1: " + str(robot.p))
                q1 += 1
            else:
                print("q2: " + str(robot.p))
                q2 += 1
        else:
            if robot.p[1] > (max_y/2):
                print("q3: " + str(robot.p))
                q3 += 1
            else:
                print("q4: " + str(robot.p))
                q4 += 1
    
    print(q1)
    print(q2)
    print(q3)
    print(q4)

    print("____________________")
    print(q1 * q2 * q3 * q4)