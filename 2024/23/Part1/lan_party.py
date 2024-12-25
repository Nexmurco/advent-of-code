with open("C:\\Users\\perki\\Documents\\GitHub\\advent-of-code\\2024\\23\\Input\\input.txt", "r") as file:
    connections = {}
    nodes = []

    for line in file:
        line = line.rstrip("\n")
        devices = line.split("-")
        n1 = devices[0]
        n2 = devices[1]
        if n1 not in connections:
            connections[n1] = set(())
        connections[n1].add(n2)

        if n2 not in connections:
            connections[n2] = set(())
        connections[n2].add(n1)

        if n1 not in nodes:
            nodes.append(n1)
        
        if n2 not in nodes:
            nodes.append(n2)
    
    cycles = set(())
    required_nodes = []
    for n1 in nodes:
        if n1[0] == "t":
            for n2 in connections[n1]:
                for n3 in connections[n2]:
                    if n1 in connections[n3]:
                        three_cycle = [n1, n2, n3]
                        three_cycle.sort()
                        cycle =(three_cycle[0], three_cycle[1], three_cycle[2])
                        cycles.add(cycle)

    for c in cycles:
        print(c)
    print(len(cycles))