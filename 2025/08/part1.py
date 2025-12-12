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
    def __hash__(self):
        return int(str(self.x) + str(self.y) + str(self.z))
    def __str__(self):
        return "[" + str(self.x) + "," + str(self.y) + "," + str(self.z) + "]"
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
    
    def __str__(self):
        c1 = self.coordinates[0]
        c2 = self.coordinates[1]
        return str(c1) + "<->" + str(c2)
    
    def get_linear_distance(self, dimension):
        c1 = self.coordinates[0]
        c2 = self.coordinates[1]
        return abs(getattr(c1, dimension) - getattr(c2, dimension))

class SortedCoordinateList:
    def __init__(self, coordinate_list, dimension):
        self.dimension = dimension
        self.coordinate_list = coordinate_list
        self.coord_to_index_map = {}
    def __init__(self, dimension):
        self.dimension = dimension
        self.coordinate_list = []
        self.coord_to_index_map = {}

    def get_coord_at(self, index):
        return self.coordinate_list[index]

    def get_coordinate_index(self, coord):
        return self.coord_to_index_map[coord]

    def _update_index_map(self):
        self.coord_to_index_map = {}
        for i in range(len(self.coordinate_list)):
            self.coord_to_index_map[self.coordinate_list[i]] = i

    def print_list(self):
        for coord in self.coordinate_list:
            print(coord)

    def print_map(self):
        for key in self.coord_to_index_map:
            print(str(key) + ": " + str(self.coord_to_index_map[key]))

    def print_dimension(self):
        print("dimension: " + self.dimension)

        

    def add_coordinate(self, coord):
        if coord in self.coord_to_index_map:
            return
        
        last_index = 0
        append_coord = True
        for index in range(len(self.coordinate_list)):
            if getattr(coord, self.dimension) < getattr(self.coordinate_list[index], self.dimension):
                append_coord = False
                break
            last_index += 1
        
        if append_coord:
            self.coordinate_list.append(coord)
            last_index = len(self.coordinate_list) - 1
        else:
            self.coordinate_list[last_index:last_index] = [coord]

        self._update_index_map()
        
        
class SearchData:
    def __init__(self):
        self.excluded_pairs = None
        self.sorted_list = None
        self.minimum_pair = None
        self.starting_index = -1
        self.direction = 0
        
        self.coordinate_pair = None

        self.index_offset = None
        self.continue_search = True

    def set_self_pair(self):
        if not self.check_out_of_bounds():
            self.coordinate_pair = None
            return self.coordinate_pair
        
        index = self.starting_index + (self.index_offset * self.direction)
        start_coord = self.sorted_list.get_coord_at(self.starting_index)
        offset_coord = self.sorted_list.get_coord_at(index)
        self.coordinate_pair = CoordinatePair(start_coord, offset_coord)

        #check for exclusions
        if check_if_pair_is_in(self.excluded_pairs, self.coordinate_pair):
            self.coordinate_pair = None

        return self.coordinate_pair
    
    def set_minimum_pair(self, min_pair):
        self.minimum_pair = min_pair
        self.check_minimum_upper_bound()

    def check_minimum_upper_bound(self):
        if self.set_self_pair() is None:
            self.continue_search = False
            return self.continue_search

        if(self.minimum_pair is not None and self.coordinate_pair.get_linear_distance(self.sorted_list.dimension) >= self.minimum_pair.distance):
            self.continue_search = False
        else:
            self.continue_search = True

        return self.continue_search
    
    def compare_minimum_distance(self):
        if not self.check_out_of_bounds():
            return self.minimum_pair
        elif not self.check_minimum_upper_bound():
            return self.minimum_pair
        elif self.minimum_pair is None or self.coordinate_pair.distance < self.minimum_pair.distance:
            self.minimum_pair = self.coordinate_pair
        
        return self.minimum_pair

    
    def set_search_offset(self, index_offset):
        self.index_offset = index_offset
        self.check_out_of_bounds()
        if self.continue_search:
            self.check_minimum_upper_bound()

    def check_out_of_bounds(self):
        index = self.starting_index + (self.index_offset * self.direction)
        if (index < 0 or index >= len(self.sorted_list.coordinate_list)):
            self.continue_search = False
        else:
            self.continue_search = True

        return self.continue_search


class MultiCoordinateList:
    def __init__(self):
        self.lists = []

    def add_coordinate_list(self, c_list):
        self.lists.append(c_list)

    def add_coordinate(self, coord):
        for l in self.lists:
            l.add_coordinate(coord)

    def get_closest_pair_with(self, coord, min_pair, excluded_pairs):
        searches = []
        for l in self.lists:
            for direction in {1, -1}:
                search_data = SearchData()
                search_data.sorted_list = l
                search_data.direction = direction
                search_data.index_offset = 1
                search_data.minimum_pair = min_pair
                search_data.starting_index = l.get_coordinate_index(coord)
                search_data.excluded_pairs = excluded_pairs
                searches.append(search_data)

        any_search_continue = True
        search_offset = 0
        new_min_pair = min_pair
        check_count = 1
        while any_search_continue and check_count < 10000:
            search_offset += 1
            any_search_continue = False
            for search in searches:
                #update search with latest info
                search.set_minimum_pair(new_min_pair)
                if not search.continue_search:
                    continue
                search.set_search_offset(search_offset)
                if not search.continue_search:
                    continue
                new_min_pair = search.compare_minimum_distance()
                any_search_continue = search.continue_search
            check_count += 1
        return new_min_pair
            

def check_if_pair_is_in(container, pair):
    for c in container:
        if pair == c:
            return True
    return False

def euclidean_dist(coord1, coord2):
    return ((coord1.x - coord2.x)**2) + ((coord1.y - coord2.y)**2) + ((coord1.z - coord2.z)**2)


def get_closest_pair(coords, exception_pairs):
    multiList = MultiCoordinateList()
    multiList.add_coordinate_list(SortedCoordinateList('y'))
    multiList.add_coordinate_list(SortedCoordinateList('z'))

    closest = None
    checked_pairs = set()

    for pair in exception_pairs:
        checked_pairs.add(pair)

    for coord in coords.coordinate_list:
        multiList.add_coordinate(coord)
        closest = multiList.get_closest_pair_with(coord, closest, checked_pairs)
    return closest
            

def find_circuits(coordinate_pairs, coordinate_id_map):
    pass


x_sorted_list = SortedCoordinateList('x')
#take puzzle input and sort on y
line_count = 0
with open(input_file, "r") as inputs:
    for input in inputs:
        line_count += 1
        line = input.rstrip()
        values = line.split(",")
        coord = Coordinate(int(values[0]), int(values[1]), int(values[2]))
        x_sorted_list.add_coordinate(coord)


#next figure out maintaining circuits and detecting if adding changes anything

#also it appears that my shortest distance is wrong for #4

x_sorted_list.print_dimension()
x_sorted_list.print_list()
print('Data Loaded\n')
pairs = set()
circuits = {}
for i in range(10):
    new_pair = get_closest_pair(x_sorted_list, pairs)
    print(new_pair)
    pairs.add(new_pair)

print()
x_sorted_list.print_map()
id_map = x_sorted_list.coord_to_index_map

id_pairs = {}
for pair in pairs:
    c1 = pair.coordinates[0]
    c2 = pair.coordinates[1]
    id_pairs[id_map[c1]] = id_map[c2]

print(id_pairs)
