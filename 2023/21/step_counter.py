from enum import Enum

visited_nodes = {}
the_grid = {}
MAX_STEPS = 64

trav_queue =[]


class Dir(Enum):
    North = 1
    East = 2
    South = 3
    West = 4


def step(pos, direction):
    if direction == Dir.North:
        return (pos[0], pos[1]-1)
    elif direction == Dir.East:
        return (pos[0]+1, pos[1])
    elif direction == Dir.South:
        return (pos[0], pos[1]+1)
    elif direction == Dir.West:
        return (pos[0]-1, pos[1])


with open("D:\\Code\\advent-of-code\\advent-of-code\\2023\\21\\input.txt", "r") as file:
    lines = list(file)
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip("\n")
        line = lines[i]
        for j in range(len(line)):
            pos = (j,i)
            node = []
            char = line[j]
            if char == "#":
                continue
            if char == "S":
                start = pos
                char = "."
            the_grid[pos] = node

for pos in the_grid.keys():
        node = the_grid[pos]
        for d in Dir:
            new_pos = step(pos, d)
            if new_pos in the_grid.keys():
                node.append(new_pos)

trav_queue.append((start, 0))


while len(trav_queue) > 0:
    trav = trav_queue.pop(0)
    pos = trav[0]
    dist = trav[1]

    if dist > MAX_STEPS:
        continue

    if pos not in visited_nodes.keys() or visited_nodes[pos] > dist:
        visited_nodes[pos] = dist
        
        #a more efficient route was found so add this pos to the queue
        #now double step and append to the trav_queue
        for p in the_grid[pos]:
            for pp in the_grid[p]:
                trav_queue.append((pp, dist+2))


print(len(visited_nodes))