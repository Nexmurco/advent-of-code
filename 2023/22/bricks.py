dimensions = ["X", "Y", "Z"]

bricks = []
with open("D:\\Code\\advent-of-code\\advent-of-code\\2023\\22\\test.txt", "r") as file:
    lines = list(file)
    for line in lines:
        line = line.rstrip("\n")
        coords = line.split("~")
        c1 = coords[0].split(",")
        c2 = coords[1].split(",")
        brick = {}
        brick["X"] = (int(c1[0]), int(c2[0]))
        brick["Y"] = (int(c1[1]), int(c2[1]))
        brick["Z"] = (int(c1[2]), int(c2[2]))
        bricks.append(brick)

for b in bricks:
    print(b)