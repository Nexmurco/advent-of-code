import math

average_weight = 1
pos_i = (0,0)
pos_f = (0,0)

def generate_edges (grid, center_pos):
    x = center_pos[0]
    y = center_pos[1]

    adj = []

    if x-1 >= 0:
        edge = {}
        edge["weight"] = int(grid[y][x-1])
        edge["pos"] = (x-1, y)
        adj.append(edge)
    if x+1 < len(grid[y]):
        edge = {}
        edge["weight"] = int(grid[y][x+1])
        edge["pos"] = (x+1, y)
        adj.append(edge)
    if y-1 >= 0:
        edge = {}
        edge["weight"] = int(grid[y-1][x])
        edge["pos"] = (x, y-1)
        adj.append(edge)
    if y+1 < len(grid):
        edge = {}
        edge["weight"] = int(grid[y+1][x])
        edge["pos"] = (x, y+1)
        adj.append(edge)

    return adj

    
def direction(new_pos, prev_pos):
    if new_pos[0] > prev_pos[0]:
        return 1
    elif new_pos[0] < prev_pos[0]:
        return 2
    elif new_pos[1] > prev_pos[1]:
        return 3
    elif new_pos[1] < prev_pos[1]:
        return 4

def is_quad_movement(new_pos, last_pos, cameFrom):
    #check the direction of movement from new_pos to last_pos
    dir = direction(new_pos, last_pos)
    for i in range(3):
        if last_pos == pos_i:
            break
        new_pos = last_pos
        last_pos = cameFrom[last_pos]
        if direction(new_pos, last_pos) != dir:
            return False
    
    return True

def dijkstra(graph):
    visited_map = {}
    dist_map_tentative = {}
    for key in graph.keys():
        visited_map[key] = False
        dist_map_tentative[key] = math.inf

    node_cur = pos_i

    for edge in node_cur["edges"]:

    





with open("D:\\Code\\Advent of Code 2023\\Dec17\\Part1\\test.txt", "r") as file:
    lines = list(file)
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip("\n")

    graph = {}
    pos_i = (0,0)
    pos_f = (len(lines[0]) - 1, len(lines) - 1)
    total_nodes = 0
    total_weight = 0
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            total_nodes += 1
            total_weight += int(lines[row][col])
            node = {}
            weight = lines[row][col]
            pos = (col, row)
            node["pos"] = pos
            node["edges"] = generate_edges(lines, pos)
            graph[pos] = node

    average_weight = total_weight/total_nodes

    for line in lines:
        print(line)
    print()
    path = a_star(pos_i, pos_f, graph)
    for step in path:
        line = lines[step[1]]
        line = line[:step[0]] + "X" + line[step[0]+1:]
        lines[step[1]] = line

    for line in lines:
        print(line)

