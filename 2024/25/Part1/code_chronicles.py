import copy
with open("C:\\Users\\perki\\Documents\\GitHub\\advent-of-code\\2024\\25\\Input\\input.txt", "r") as file:
    sections = []
    
    reset = True
    for line in file:
        line = line.rstrip("\n")
        
        if line == "":
            sections.append(section)
            reset = True
            continue

        if reset:
            reset = False
            section = []
        
        section.append(line)
    

    lock_schematics = {}
    key_schematics = {}

    lock_heights = {}
    key_heights = {}

    lock_id = 0
    key_id = 0

    lock_top_row = "#####"
    key_top_row = "....."

    for s in sections:
        # for s1 in s:
            # print(s1)

        if s[0] == lock_top_row:
            # print("lock")
            heights = []
            for x in range(len(s[0])):
                for y in range(len(s)):
                    if s[y][x] == ".":
                        heights.append(y - 1)
                        break

            lock_heights[lock_id] = copy.copy(heights)
            lock_id += 1

        elif s[0] == key_top_row:
            # print("key")
            heights = []
            for x in range(len(s[0])):
                for y in range(len(s)):
                    if s[y][x] == "#":
                        heights.append(6 - y)
                        break

            key_heights[key_id] = copy.copy(heights)
            key_id += 1
        # print(heights)

    # print("locks")
    # print(str(lock_heights.values()))
    # print()
    # print("keys")
    # print(str(key_heights.values()))

    # print()
    valid_pairs = []
    for j, lock in lock_heights.items():
        for i, key in key_heights.items():
            # print("lock - key")
            # print(str(lock))
            # print(str(key))
            valid_pair = True
            for k in range(5):
                if key[k] + lock[k] >= 6:
                    valid_pair = False
                    # print("invalid in col " + str(k))
                    break
                
            
            if valid_pair:
                # print("valid pair")
                valid_pairs.append((lock, key))
    
            # print()

    for p in valid_pairs:
        print(p)
    
    print(len(valid_pairs))
