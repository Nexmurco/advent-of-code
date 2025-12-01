from enum import Enum
import copy
import math
from dataclasses import dataclass

def tuple_add(a, b):
    val = (a[0] + b[0], a[1] + b[1])
    return val

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

def is_in_bounds(pos):
    global max_x
    global max_y
    return (pos[0] < max_x and pos[0] >= 0 and pos[1] < max_y and pos[1] >= 0)

with open("C:\\Users\\perki\\Documents\\GitHub\\advent-of-code\\2024\\18\\Input\\input.txt", "r") as file:
    max_x = 71
    max_y = 71
    max_bytes = 1024

    pos_start = (0, 0)
    pos_end = (max_x - 1, max_y - 1)
    nodes = {}
    spaces = []
    walls = []
    grid = []
    
    
    count = 0
    for line in file:
        count += 1

        line = line.rstrip("\n")
        coords = line.split(",")
        pos = (int(coords[0]), int(coords[1]))
        walls.append(pos)

        if count >= max_bytes:
            break


    for y in range(max_y):
        row = []
        string = ""
        for x in range(max_x):
            if (x,y) in walls:
                char = "#"
            else:
                spaces.append((x,y))
                char = "."
            
            row.append(char)
            string += char
        grid.append(row)

    



    unvisited_nodes = set(())

    for space in spaces:
        adjacent_nodes = []
        for d in Dir:

            #if its a space, construct
            adj_space = tuple_add(space, movement[d])
            if adj_space in spaces:
                adjacent_nodes.append((adj_space, 1))

            if space == pos_start:
                distance = 0
            else:
                distance = math.inf

        

        unvisited_nodes.add(space)
        nodes[space] = Node(space, adjacent_nodes, distance)


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
            adj_node = nodes[edge[0]]
            edge_weight = edge[1]
            tent_distance = current_node.distance + edge_weight
            
            if tent_distance < adj_node.distance:
                adj_node.distance = tent_distance
            
        #remove current node from unvisited set
        unvisited_nodes.remove(current_node.pos)
    
    dist = nodes[pos_end].distance
    

    print(dist)
