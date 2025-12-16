from collections import deque
import copy
import sys
input_file = sys.argv[1]

def drop(pos):
    if not is_in_bounds(pos):
        count = 1
        pos_count_map[pos] = count
        return count
    if pos in pos_count_map:
        return pos_count_map[pos]
    if pos in splitter_list:
        count = drop(go_right(pos)) + drop(go_left(pos))
        pos_count_map[pos] = count
        return count
    else:
        count = drop((pos[0]+1, pos[1]))
        pos_count_map[pos] = count
        return count


def go_right(pos):
    return (pos[0], pos[1]+1)

def go_left(pos):
    return (pos[0], pos[1]-1)

def is_in_bounds(pos):
    if pos[0] >= upper_bounds[0] or pos[1] >= upper_bounds[1] or pos[0] < 0 or pos[1] < 0:
        return False
    return True


grid = []
with open(input_file, "r") as input_lines:
    for row in input_lines:
        grid.append(row.rstrip())


s_pos = None
pos_count_map = {}
splitter_list = []
upper_bounds = (len(grid), len(grid[0]))

for row in range(len(grid)):
    line = grid[row]
    for col in range(len(line)):
        if line[col] == "^":
            splitter_list.append((row, col))
        if line[col] == "S":
            s_pos = (row, col)

splitter_list.sort(reverse=True)

for position in splitter_list:
    drop(position)

total = drop(s_pos)
print(total)

# #alternates:
# #investigate topological sorting solution
# #https://www.geeksforgeeks.org/dsa/count-possible-paths-two-vertices/