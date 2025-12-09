import sys
input_file = sys.argv[1]    

class Coordinate:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z
    def __lt__(self, other):
        if self.x < other.x:
            return True
        elif self.x == other.x and self.y < other.y:
            return True
        elif self.y == other.y and self.z < other.z:
            return True 
        return False
    def get_coordinates(self):
        return(self.x, self.y, self.z)

class CoordinatePair:
    def __init__(self, c1, c2):
        self.coordinates = tuple(sorted([c1, c2]))
        self.distance = euclidean_dist(c1, c2)
    def __eq__(self, other):
        return self.coordinates[0] == other.coordinates[0] and self.coordinates[1] == other.coordinates[1]
    def __lt__(self, other):
        if  self.coordinates[0] < other.coordinates[0]:
            return True
        if self.coordinates[0] == other.coordinates[0] and self.coordinates[1] < other.coordinates[1]:
            return True
        return False
    def __hash__(self):
        c1 = self.coordinates[0]
        c2 = self.coordinates[1]
        return int(str(c1.x)+str(c1.y)+str(c1.z)+str(c2.x)+str(c2.y)+str(c2.z))

def check_if_pair_is_in(container, pair):
    for c in container:
        if pair == c:
            return True
    return False

def euclidean_dist(coord_tuple):
    return euclidean_dist(coord_tuple[0], coord_tuple[1])

def euclidean_dist(coord1, coord2):
    return ((coord1.x - coord2.x)**2) + ((coord1.y - coord2.y)**2) + ((coord1.z - coord2.z)**2)

def terminate_search_y(min_pair, coord_list, base_coord, base_index, offset):
    new_index = base_index + offset
    if new_index < 0 or new_index >= len(coord_list):
        return True
    new_coord = coord_list[new_index]
    y_dist = abs(base_coord.y - new_coord.y)

    if min_pair is not None and min_pair.distance > y_dist:
        return True

def terminate_search_z(min_pair, coord_list, base_coord, base_index, offset):
    new_index = base_index + offset
    if new_index < 0 or new_index >= len(coord_list):
        return True
    new_coord = coord_list[new_index]
    z_dist = abs(base_coord.z - new_coord.z)

    if min_pair is not None and min_pair.distance > z_dist:
        return True

def get_min_pair(min_pair, coord_list, base_coord, base_index, offset, exceptions):

    new_index = base_index + offset
    new_coord = coord_list[new_index]
    dist = euclidean_dist(base_coord, new_coord)
    
    new_pair = CoordinatePair(base_coord, new_coord)
    
    if check_if_pair_is_in(exceptions, new_pair):
        return min_pair
    
    print("Comparing:")
    print(str(new_coord.get_coordinates()) + "<->" + str(base_coord.get_coordinates()) + ": " + str(dist))
    
    exceptions.add(new_pair)

    if min_pair is None or dist < min_pair.distance:
        return new_pair
    
    return min_pair
    

def insert_into_sorted_y(s_list, new_value):
    last_index = 0
    append_coord = True
    for index in range(len(s_list)):
        if new_value.y < s_list[index].y:
            append_coord = False
            break
        last_index += 1
    
    if append_coord:
        s_list.append(new_value)
        last_index = len(s_list) - 1
    else:
        s_list[last_index:last_index] = [new_value]
    
    return last_index

def insert_into_sorted_z(s_list, new_value):
    last_index = 0
    append_coord = True
    for index in range(len(s_list)):
        if new_value.z < s_list[index].z:
            append_coord = False
            break
        last_index += 1
    
    if append_coord:
        s_list.append(new_value)
        last_index = len(s_list) - 1
    else:
        s_list[last_index:last_index] = [new_value]
    
    return last_index


def get_closest_pair(coords, exception_pairs):
    sorted_y = []
    sorted_z = []
    smallest_pair = None
    checked_pairs = set()

    for pair in exception_pairs:
        checked_pairs.add(pair)

    for coord in coords:
        #add value into sorted y
        print("new coord: " + str(coord.get_coordinates()))
        inserted_y = insert_into_sorted_y(sorted_y, coord)
        inserted_z = insert_into_sorted_z(sorted_z, coord)

        #go up and down the lists while the y-distance and z-distance is smaller than smallest_distance
        #updating smallest distance with best found value
        y_ascend = True
        y_descend = True
        z_ascend = True
        z_descend = True

        index_jump = 1


        while y_ascend or y_descend or z_ascend or z_descend:

            y_descend = not terminate_search_y(smallest_pair, sorted_y, coord, inserted_y, -index_jump)
            y_ascend = not terminate_search_y(smallest_pair, sorted_y, coord, inserted_y, index_jump)
            z_descend = not terminate_search_z(smallest_pair, sorted_z, coord, inserted_y, -index_jump)
            z_ascend = not terminate_search_z(smallest_pair, sorted_z, coord, inserted_y, index_jump)

            if y_descend:
                smallest_pair = get_min_pair(smallest_pair, sorted_y, coord, inserted_y, -index_jump, checked_pairs)
            if y_ascend:
                smallest_pair = get_min_pair(smallest_pair, sorted_y, coord, inserted_y, index_jump, checked_pairs)
            if z_descend:
                smallest_pair = get_min_pair(smallest_pair, sorted_z, coord, inserted_z, -index_jump, checked_pairs)
            if z_ascend:
                smallest_pair = get_min_pair(smallest_pair, sorted_z, coord, inserted_z, index_jump, checked_pairs)
            
            index_jump += 1

        print("Smallest Pair Found:")
        if smallest_pair is not None:
            print(str(smallest_pair.coordinates[0].get_coordinates()) + "<->" + str(smallest_pair.coordinates[1].get_coordinates()) + ": " + str(smallest_pair.distance))
        else:
            print(smallest_pair)
        print()
    
    return smallest_pair
            

coordinates = []
#take puzzle input and sort on y
line_count = 0
with open(input_file, "r") as inputs:
    for input in inputs:
        line_count += 1
        line = input.rstrip()
        values = line.split(",")
        coord = Coordinate(int(values[0]), int(values[1]), int(values[2]))
        coordinates.append(coord)


coordinates.sort()
for c in coordinates:
    print(c.x, c.y, c.z)
get_closest_pair(coordinates, set())
