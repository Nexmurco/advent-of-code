with open("D:\\Code\\advent-of-code\\advent-of-code\\2023\\19\\test.txt", "r") as file:
    lines = list(file)

    isFirst = True
    
    rules = {}
    parts = []

    for line in lines:
        line = line.rstrip("\n")
        
        if isFirst:
            if line == "":
                isFirst = False
                continue

            line = line.replace("}","")
            input = line.split("{")
            key = input[0]
            line = input[1].split(",")
            print(key)
            #print(line)
            commands = []
            for c in range(len(line)):
                com = line[c]
                if c == len(line)-1:
                    command = {}
                    command["parameter"] = None
                    command["destination"] = com
                    commands.append(command)
                else:
                    parameter = com[0]
                    operation = com[1]
                    c2 = com[2:].split(":")
                    threshold = c2[0]
                    destination = c2[1]

                    command = {}
                    command["parameter"] = parameter
                    command["operation"] = operation
                    command["threshold"] = int(threshold)
                    command["destination"] = destination
                    commands.append(command)
            
            print(commands)
            rules[key] = commands
            print()
    
        else:
            part = {}
            line = line.replace("{", "").replace("}", "")
            p = line.split(",")

            for i in p:
                part[i[0]] = int(i[2:])
            print(part)

            parts.append(part)

    print(len(parts))


    total = 0

    for part in parts:
        print()
        print(part)
        key = "in"

        while True:
            print("key: " + str(key))
            
            if key == "A" or key == "R":
                break

            

            for r in range(len(rules[key])):
                
                rule = rules[key][r]

                if r == (len(rules[key]) - 1):
                    key = rule["destination"]
                    break


                param = part[rule["parameter"]]
                threshold = rule["threshold"]
                op = rule["operation"]
                if op == "<":
                    param *= -1
                    threshold *= -1
                
                if param > threshold:
                    key = rule["destination"]
                    break
        
        if key == "A":
            for key in part.keys():
                total += part[key]

            print(total)
        
    print(total)
    for r in rules.keys():
        print(r)
        for i in rules[r]:
            print(i)
        print()



            
        





