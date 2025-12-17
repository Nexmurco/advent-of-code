import sys
input_file = sys.argv[1]

def calc_area(pos1, pos2):
    return (abs(pos1[0] - pos2[0])) * (abs(pos1[1] - pos2[1]))

def calc_area_final(pos1, pos2):
    return (abs(pos1[0] - pos2[0]) + 1) * (abs(pos1[1] - pos2[1]) + 1)

coordinates = []

with open(input_file, "r") as input_lines:
    for line in input_lines:
        coord = line.rstrip().split(",")
        coordinates.append((int(coord[0]), int(coord[1])))
    

coords_x = sorted(coordinates, key=lambda point:point[0])
coords_y = sorted(coordinates, key=lambda point:point[1])
span_x = abs(coords_x[0][0] - coords_x[-1][0])
span_y = abs(coords_y[0][1] - coords_y[-1][1])
print(coords_x)
print(span_x)
print()
print(coords_y)
print(span_y)
print()

max_area = 0
pair = None
for p1 in coords_x:
    for p2 in coords_x:
        area = calc_area(p1,p2)
        if area > max_area:
            max_area = area
            pair = (p1,p2)

print(max_area)
print(pair)
print(calc_area_final(pair[0], pair[1]))

#multiply first x value by all values