from collections import deque
import sys
input_file = sys.argv[1]

def drop(pos):
    return (pos[0]+1, pos[1])

def go_right(pos):
    return (pos[0], pos[1]+1)

def go_left(pos):
    return (pos[0], pos[1]-1)

def is_in_bounds(pos, upper_bounds):
    if pos[0] >= upper_bounds[0] or pos[1] >= upper_bounds[1] or pos[0] < 0 or pos[1] < 0:
        return False
    return True


grid = []
with open(input_file, "r") as input_lines:
    for row in input_lines:
        grid.append(row.rstrip())

s_pos = None
splitter_pos = set()
upper_bound = (len(grid), len(grid[0]))

for row in range(len(grid)):
    line = grid[row]
    for col in range(len(line)):
        if line[col] == "^":
            splitter_pos.add((row, col))
        if line[col] == "S":
            s_pos = (row, col)

splitter_count = 0
continue_beam = True

used_beam_pos = set()
beams = deque()
beams.append(drop(s_pos))


beam_count = 0
while len(beams) > 0:
    beam_count += 1
    beam = beams.popleft()
    
    if not is_in_bounds(beam, upper_bound):
        continue
    if beam in used_beam_pos:
        continue

    used_beam_pos.add(beam)

    if beam in splitter_pos:
        splitter_count += 1
        beams.append(go_left(beam))
        beams.append(go_right(beam))
    else:
        beams.append(drop(beam))
    
    if beam_count >= 10000:
        break

print(splitter_count)