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
                if (get_limit(elements[1]) is not None and int(elements[0]) > get_limit(elements[1])):
                    is_possible = False

        if is_possible:
            sum += turn_counter

        turn_counter += 1

    print(sum)

            
                