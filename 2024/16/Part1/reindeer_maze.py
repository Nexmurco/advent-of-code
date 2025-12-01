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

clockwise = {
    Dir.North: Dir.East,
    Dir.East: Dir.South,
    Dir.South: Dir.West,
    Dir.West: Dir.North
}

counterclockwise = {
    Dir.North: Dir.West,
    Dir.East: Dir.North,
    Dir.South: Dir.East,
    Dir.West: Dir.South
}

@dataclass
class Node:
    pos: tuple
    facing: Dir
    adjacencies: list[tuple]
    distance: int


with open("C:\\Users\\perki\\Documents\\GitHub\\advent-of-code\\2024\\16\\Input\\input.txt", "r") as file:
    pos_start = (-1,-1)
    pos_end = (-1,-1)
    facing_start = Dir.East
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
        for d in Dir:
            #construct the key
            key_tuple = (space, d)

            adjacent_nodes = []

            #construct rotational adjacencies
            adjacent_nodes.append((space, clockwise[d], 1000))
            adjacent_nodes.append((space, counterclockwise[d], 1000))

            #if its a space, construct
            adj_space = tuple_add(space, movement[d])
            if adj_space in spaces:
                adjacent_nodes.append((adj_space, d, 1))

            if space == pos_start and d == facing_start:
                distance = 0
            else:
                distance = math.inf
            
            unvisited_nodes.add(key_tuple)
            nodes[key_tuple] = Node(space, d, adjacent_nodes, distance)


    while len(unvisited_nodes) > 0:
        if len(unvisited_nodes) % 1000 == 0:
            print("remaining nodes: " + str(len(unvisited_nodes)))
        #select unvisited node with the smallest distance
        min_dist = math.inf
        current_node = None
        for key_tuple in unvisited_nodes:
            n = nodes[key_tuple]
            if n.distance < min_dist:
                current_node = n
                min_dist = n.distance
        
        if current_node is None:
            break
        
        for edge in current_node.adjacencies:
            #update distances if a shorter one exists
            adj_node = nodes[(edge[0], edge[1])]
            edge_weight = edge[2]
            tent_distance = current_node.distance + edge_weight
            
            if tent_distance < adj_node.distance:
                adj_node.distance = tent_distance
            
        #remove current node from unvisited set
        unvisited_nodes.remove((current_node.pos, current_node.facing))
    
    dist = math.inf
    for d in Dir:
        n = nodes[(pos_end, d)]
        if n.distance < dist:
            dist = n.distance
    

    print(dist)
