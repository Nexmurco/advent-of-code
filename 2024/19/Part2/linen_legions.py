def search(string):
    global pattern_dict
    global matches

    if string == "":
        matches += 1
        print("matches found: " + str(matches))
        return

    char = string[0]

    for pattern in pattern_dict[char]:
        if pattern == string[:len(pattern)]:
            search(string[len(pattern):])
    
    return




with open("C:\\Users\\perki\\Documents\\GitHub\\advent-of-code\\2024\\19\\Input\\input_test.txt", "r") as file:
    get_basis = True
    
    patterns = []
    pattern_dict = {}
    pattern_dict["r"] = []
    pattern_dict["g"] = []
    pattern_dict["u"] = []
    pattern_dict["b"] = []
    pattern_dict["w"] = []
    designs = []

    for line in file:
        line = line.rstrip("\n")
        
        if get_basis:
            line = line.split(", ")
            for pattern in line:
                patterns.append(pattern)
                first_char = pattern[0]
                pattern_dict[first_char].append(pattern)
            get_basis = False
        else:
            if line == "":
                pass
            else:
                designs.append(line)
    
    # for d in designs:
    #     print(d)
    
    # for key in pattern_dict:
    #     print(key + ": " + str(pattern_dict[key]))


    matches = 0
    design_count = 0
    for d in designs:
        design_count += 1
        print(design_count)
        match_found = False
        search(d)
        if match_found:
            matches += 1
    
    print(matches)