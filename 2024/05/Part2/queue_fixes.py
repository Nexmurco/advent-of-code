with open("C:\\Users\\perki\\Documents\\GitHub\\advent-of-code\\2024\\05\\Input\\input.txt", "r") as file:
    
    sum = 0

    lines = []

    input_rules = True
    rules_ge = {}
    rules_le = {}
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
            if page_pre not in rules_ge:
                rules_ge[page_pre] = []
            rules_ge[page_pre].append(page_post)

            if page_post not in rules_le:
                rules_le[page_post] = []
            rules_le[page_post].append(page_pre)
        else:
            updates.append(line)


    print("greater rules: ")
    for valid_rule in rules_ge:
        print(str(valid_rule) + ": " + str(rules_ge[valid_rule]))

    print("lesser rules: ")
    for invalid_rule in rules_le:
        print(str(invalid_rule) + ": " + str(rules_le[invalid_rule]))


    update_id = 0
    invalid_updates = {}
    invalid_combos = {}

    for update in updates:
        print()
        is_valid_update = True
        print("scanning update: " + str(update))
        pages = update.split(",")
        for i in range(len(pages)):
            p1 = pages[i]
            for j in range(i+1, len(pages)):
                p2 = pages[j]
                if p1 in rules_le and p2 in rules_le[p1]:
                    print("page invalid with pairing: " + str(p1) + " " + str(p2))
                    if update_id not in invalid_combos:
                        invalid_combos[update_id] = []
                    invalid_combos[update_id].append((p1, p2))
                    is_valid_update = False
        
        if not is_valid_update:
            print("update is valid")
            invalid_updates[update_id] = update
            update_id += 1
    
    print()

    #now fix the invalid updates
    for uid in invalid_updates:
        update = invalid_updates[uid]

        page_scoring = {}

        #check every combo for rules on ordering and make greater and lesser subsets
        print("fixing update: " + str(update))
        
        print("invalid combos:")
        for mismatch in invalid_combos[uid]:
            print(mismatch)
        
        pages = update.split(",")
        subrules_g = {}
        subrules_l = {}
        for i in range(len(pages)):
            p1 = pages[i]
            
            page_scoring[p1] = 0

            for j in range(i+1, len(pages)):
                p2 = pages[j]

                if p1 in rules_ge and p2 in rules_ge[p1]:
                    if p1 not in subrules_g:
                        subrules_g[p1] = []
                    subrules_g[p1].append(p2)
                if p2 in rules_ge and p1 in rules_ge[p2]:
                    if p2 not in subrules_g:
                        subrules_g[p2] = []
                    subrules_g[p2].append(p1)

                if p2 in rules_le and p1 in rules_le[p2]:
                    if p2 not in subrules_l:
                        subrules_l[p2] = []
                    subrules_l[p2].append(p1)
                if p1 in rules_le and p2 in rules_le[p1]:
                    if p1 not in subrules_l:
                        subrules_l[p1] = []
                    subrules_l[p1].append(p2)
        
        print("subrules greater: ")
        for sr in subrules_g:
            page_scoring[sr] -= len(subrules_g[sr])
            print(str(sr) + ": " + str(subrules_g[sr]))
        
        print("subrules lesser: ")
        for sr in subrules_l:
            page_scoring[sr] += len(subrules_l[sr])
            print(str(sr) + ": " + str(subrules_l[sr]))
        
        print()

        page_scoring = dict(sorted(page_scoring.items(), key=lambda item: item[1]))
        print(page_scoring)

        corrected_update = []
        for key in page_scoring:
            corrected_update.append(key)
        
        sum += int(corrected_update[(int(len(corrected_update)/2))])

    print(sum)