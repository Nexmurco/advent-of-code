from enum import Enum
import copy
import math
from dataclasses import dataclass

def tuple_add(a, b):
    val = (a[0] + b[0], a[1] + b[1])
    return val

def coord_dist(coord1, coord2):
    dx = abs(coord1[0] - coord2[0])
    dy = abs(coord1[1] - coord2[1])
    return dx + dy

class Dir(Enum):
    North = 1
    East = 2
    South = 3
    West = 4

movement = {
    Dir.North: (0,-1),
    Dir.East: (1,0),
    Dir.South: (0,1),
    Dir.West: (-1,0)
}

@dataclass
class Node:
    pos: tuple
    adjacencies: list[tuple]
    distance: int

with open("C:\\Users\\perki\\Documents\\GitHub\\advent-of-code\\2024\\20\\Input\\input.txt", "r") as file:
    pos_start = (-1, -1)
    pos_end = (-1, -1)
    nodes = {}
    spaces = []
    walls = []
    grid = []
    
    for line in file:
        line = line.rstrip("\n")
        row = []
        for l in line:
            row.append(l)
        grid.append(row)
    
    for y in range(len(grid)):
        row = grid[y]
        for x in range(len(row)):
            char = row[x]
            if char == ".":
                spaces.append((x,y))
            elif char == "#":
                walls.append((x,y))
            elif char == "S":
                spaces.append((x,y))
                pos_start = (x,y)
            elif char == "E":
                spaces.append((x,y))
                pos_end = (x,y)
    
    unvisited_nodes = set(())
    
    for space in spaces:
        distance = math.inf
        if space == pos_start:
            distance = 0
        adjacent_nodes = []
        for d in Dir:
            adj_space = tuple_add(space, movement[d])
            if adj_space in spaces:
                adjacent_nodes.append(adj_space)   
            
        nodes[space] = Node(space, adjacent_nodes, distance)
        unvisited_nodes.add(space)

    print("spaces")
    print(spaces)
    print("walls")
    print(walls)

    print()
    print("start and end")
    print(pos_start)
    print(pos_end)
    print()


    print("unvisited spaces")
    print(unvisited_nodes)

    prev_pos_dict = {}

    #dijkstra's alg
    while len(unvisited_nodes) > 0:
        #select unvisited node with the smallest distance
        min_dist = math.inf
        current_node = None
        for pos in unvisited_nodes:
            n = nodes[pos]
            if n.distance < min_dist:
                current_node = n
                min_dist = n.distance
        
        if current_node is None:
            break
        
        for edge in current_node.adjacencies:
            #update distances if a shorter one exists
            adj_node = nodes[edge]
            tent_distance = current_node.distance + 1
            
            if tent_distance < adj_node.distance:
                prev_pos_dict[adj_node.pos] = current_node.pos
                adj_node.distance = tent_distance
            
        #remove current node from unvisited set
        unvisited_nodes.remove(current_node.pos)
    
    dist = nodes[pos_end].distance
    
    #now construct the shortest path using prev dict

    path = []

    pos_curr = pos_end
    pos_prev = pos_end

    path.append(pos_curr)
    while pos_curr != pos_start:
        print(pos_curr)
        pos_prev = pos_curr
        pos_curr = prev_pos_dict[pos_prev]
        path.append(pos_curr)

    path.reverse()
    print(path)
    print(dist)

    #for each pair of coordinates, find if they are within 2 steps of each other
    #then subtract the distance by the distance saved of the cheat

    save_dict = {}
    saves = 0

    for i in range(len(path)):
        coord_i = path[i]
        d1 = nodes[coord_i].distance
        for j in range(i+1, len(path)):
            coord_j = path[j]
            d2 = nodes[coord_j].distance
            if coord_dist(coord_i, coord_j) == 2:
                distance_save = abs(d1 - d2) - 2
                if distance_save >= 100:
                    saves += 1
                    if distance_save not in save_dict:
                        save_dict[distance_save] = 0
                    save_dict[distance_save] += 1

    print(save_dict)
    print(saves)