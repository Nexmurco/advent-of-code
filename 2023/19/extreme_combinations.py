def narrow_zone(rules, key, zone):
    commands = rules[key]

    for command in commands:
        #if possible, start with affirming the case is true
        key = command["destination"]
        narrow_zone(rules, key, zone)
        #negate the case then continue


with open("D:\\Code\\advent-of-code\\advent-of-code\\2023\\19\\test.txt", "r") as file:
    lines = list(file)
    rules = {}

    for line in lines:
        line = line.rstrip("\n")
        

        if line == "":
            break

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
            
        rules[key] = commands

    

    zone = {"x": [], "m": [], "a": [], "s": []}
    narrow_zone(rules, "in", zone)

    



            
        





