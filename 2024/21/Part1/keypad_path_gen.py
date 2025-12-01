keypad_numeric = [[7, 8, 9], [4, 5, 6], [1, 2, 3], [None, 0, "A"]]
keypad_directional = [[None, "^", "A"], ["<", "v", ">"]]


with open("C:\\Users\\perki\\Documents\\GitHub\\advent-of-code\\2024\\21\\Supplements\\paths_numeric.txt", "w") as f:
    
    f.write("numeric_dict = {")

    for j in range(4):
        for i in range(3):
            coord1 = (i,j)
            symbol1 = keypad_numeric[j][i]
            for y in range(4):
                for x in range(3):
                    coord2 = (x,y)
                    symbol2 = keypad_numeric[y][x]
                    if coord1 == coord2:
                        continue
                    if symbol1 == None:
                        continue
                    if symbol2 == None:
                        continue
                    #prioritize going up first then right then down then left
                    direction_string = ""
                    if j > y:
                        for m in range(j - y):
                            direction_string += "^"
                    if x > i:
                        for m in range(x - i):
                            direction_string += ">"
                    if y > j:
                        for m in range(y - j):
                            direction_string += "v"
                    if i > x:
                        for m in range(i - x):
                            direction_string += "<"
                    f.write("(\"" + str(symbol1) +"\", \"" + str(symbol2) + "\"): \"" + direction_string + "\"")
                    if symbol1 == "A" and symbol2 == 0:
                        continue
                    f.write(", ")

                    #
    f.write("}")

f.close()


with open("C:\\Users\\perki\\Documents\\GitHub\\advent-of-code\\2024\\21\\Supplements\\paths_directional.txt", "w") as f:

    f.write("direction_dict = {")
    for j in range(2):
        for i in range(3):
            coord1 = (i,j)
            symbol1 = keypad_directional[j][i]
            for y in range(2):
                for x in range(3):
                    coord2 = (x,y)
                    symbol2 = keypad_directional[y][x]
                    if coord1 == coord2:
                        continue
                    if symbol1 == None:
                        continue
                    if symbol2 == None:
                        continue
                    #prioritize going up first then right then down then left
                    direction_string = ""
                    if x > i:
                        for m in range(x - i):
                            direction_string += ">"
                    if y > j:
                        for m in range(y - j):
                            direction_string += "v"
                    if i > x:
                        for m in range(i - x):
                            direction_string += "<"
                    if j > y:
                        for m in range(j - y):
                            direction_string += "^"
                    f.write("(\"" + str(symbol1) +"\", \"" + str(symbol2) + "\"): \"" + direction_string + "\"")
                    if symbol1 == ">" and symbol2 == "v":
                        continue
                    f.write(", ")
    f.write("}")

f.close()