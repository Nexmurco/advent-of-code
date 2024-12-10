with open("C:\\Users\\perki\\Documents\\GitHub\\advent-of-code\\2024\\05\\Input\\input.txt", "r") as file:
    
    sum = 0

    lines = []

    input_rules = True
    rules = {}
    invalid_rules = {}
    updates = []

    for line in file:
        line = line.rstrip("\n")
        if line == "":
            input_rules = False
            continue
        if input_rules:
            rule = line.split("|")
            page_pre = rule[0]
            page_post = rule[1]
            if page_pre not in rules:
                rules[page_pre] = []
            rules[page_pre].append(page_post)

            if page_post not in invalid_rules:
                invalid_rules[page_post] = []
            invalid_rules[page_post].append(page_pre)
        else:
            updates.append(line)

    valid_updates = []

    print("invalid rules: ")
    for invalid_rule in invalid_rules:
        print(str(invalid_rule) + ": " + str(invalid_rules[invalid_rule]))


    for update in updates:
        print()
        is_valid_update = True
        print("scanning update: " + str(update))
        pages = update.split(",")
        for i in range(len(pages)):
            p1 = pages[i]
            for j in range(i+1, len(pages)):
                p2 = pages[j]
                if p1 in invalid_rules and p2 in invalid_rules[p1]:
                    print("page invalid with pairing: " + str(p1) + " " + str(p2))
                    is_valid_update = False
                    break
            
            if not is_valid_update:
                break
        
        if is_valid_update:
            print("update is valid")
            valid_updates.append(update)
    


    for update in valid_updates:
        values = update.split(",")
        print("adding update: " + str(values))
        value = int(values[int(len(values)/2)])
        print(value)
        sum += value
    print(sum)