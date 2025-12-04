import sys
input_file = sys.argv[1]

bool_grid = []
adj_grid = []
adj_positions = [-1,0,1]

#take puzzle input and make a 2d list showing positions
with open(input_file, "r") as inputs:
    for input in inputs:
        line = input.rstrip()
        row = []
        for char in line:
            if char == "@":
                row.append(True)
            else:
                row.append(False)
        bool_grid.append(row)


count_rows = len(bool_grid)
count_cols = len(bool_grid[0])


for i in range(count_rows):
    adj_grid.append([0] * count_cols)

for i in range(count_rows):
    for j in range(count_cols):
        if bool_grid[i][j]:
            #go in each direction and add 1
            for x in adj_positions:
                #do not go out of bounds
                if i == 0 and x == -1:
                    continue
                if i == count_rows-1 and x == 1:
                    continue

                for y in adj_positions:
                    #do not add to the current space
                    if y == 0 and x == 0:
                        continue
                    #do not go out of bounds
                    if j == 0 and y == -1:
                        continue
                    if j == count_cols-1 and y == 1:
                        continue
                    adj_grid[i+x][j+y] += 1

sum = 0
clearance = 4
for i in range(count_rows):
    for j in range(count_cols):
        if bool_grid[i][j] == True and adj_grid[i][j] < 4:
            sum += 1

print(sum)
