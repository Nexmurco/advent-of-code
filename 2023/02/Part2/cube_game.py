limit_r = 12
limit_g = 13
limit_b = 14

def get_limit(color):
    if color == "green":
        return limit_g
    elif color == "red":
        return limit_r
    elif color == "blue":
        return limit_b
    
    return None



with open("input.txt", "r") as file:
    sum = 0
    turn_counter = 1
    for line in file:
        #game level
        power = 1
        min_r = 0
        min_b = 0
        min_g = 0
        turns = line.replace(":",";").split("; ")
        is_possible = True
        for turn in turns:
            #turn level
            cube_list = []
            cubes = turn.replace(", ",",").split(",")
            for cube in cubes:
                cube = cube.replace("\n","")
                #draw level
                elements = cube.split(" ")
                if (elements[1] == "red"):
                    min_r = max(int(elements[0]), min_r)
                elif (elements[1] == "green"):
                    min_g = max(int(elements[0]), min_g)
                elif (elements[1] == "blue"):
                    min_b = max(int(elements[0]), min_b)

        sum += min_b*min_g*min_r

        turn_counter += 1

    print(sum)    