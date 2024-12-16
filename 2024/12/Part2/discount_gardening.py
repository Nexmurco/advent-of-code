from enum import Enum
import copy

def collect_region(plot, region_array):
    global pos_plot_dict
    global used_pos

    if plot.pos in used_pos:
        return
    else:

        used_pos.add(plot.pos)
        region_array.append(plot.pos)
    
    for d in Dir:
        new_pos = add(plot.pos, movement[d])
        if plot.adjacencies[d] == None or not is_in_bounds(new_pos):
            continue
        collect_region(pos_plot_dict[new_pos], region_array)


def add(a, b):
    val = (a[0] + b[0], a[1] + b[1])
    return val

def is_in_bounds(pos):
    global max_x
    global max_y
    return pos[0] < max_x and pos[0] >= 0 and pos[1] < max_y and pos[1] >= 0

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

adjacency_dict = {
    Dir.North: None,
    Dir.East: None,
    Dir.South: None,
    Dir.West: None
}

class Plot:
    adjacencies = {}
    plant = None
    pos = None

with open("C:\\Users\\perki\\Documents\\GitHub\\advent-of-code\\2024\\12\\Input\\input_test.txt", "r") as file:
    lines = []
    for line in file:
        line = line.rstrip("\n")
        lines.append(line)


    max_x = len(lines[0])
    max_y = len(lines)

    plots = []
    pos_plot_dict = {}
    for y in range(len(lines)):
        line = lines[y]
        for x in range(len(line)):
            plot = Plot()
            plot.adjacencies = copy.copy(adjacency_dict)
            plot.plant = line[x]
            pos = (x,y)
            plot.pos = pos
            pos_plot_dict[pos] = plot
            for d in Dir:
                new_pos = add(pos, movement[d])
                new_plant = None
                if is_in_bounds(new_pos):
                    new_plant = lines[new_pos[1]][new_pos[0]]
                else:
                    continue
                if new_plant == plot.plant:
                    plot.adjacencies[d] = new_pos

    region_id = -1
    region_dict = {}
    id_letter_dict = {}
    used_pos = set(())
    current_plant = None
    
    for key in pos_plot_dict:
        plot = pos_plot_dict[key]
        if plot.pos not in used_pos:
            current_plant = plot.plant
            region_id += 1
            region_dict[region_id] = []
            id_letter_dict[region_id] = current_plant
            collect_region(plot, region_dict[region_id])



    sum = 0
    for key in region_dict:
        #for each region, construct a secondary grid of 
        region = region_dict[key]

        pos_list1 = []
        pos_list2 = []
        for pos in region:
            plot = pos_plot_dict[pos]
            for d, p in plot.adjacencies.items():
                if p is None:
                    adj_pos = add(pos, movement[d])
                    pos_list1.append(adj_pos)
                    pos_list2.append((adj_pos[1], adj_pos[0]))
        print()
        print(id_letter_dict[key] + str(key))
        pos_list1.sort()
        pos_list2.sort()
        print(pos_list1)
        print(pos_list2)

        sides = 0
        
        prev = pos_list1[0]
        for i in range(1, len(pos_list1)):
            curr = pos_list1[i]
            if


    print(sum)
