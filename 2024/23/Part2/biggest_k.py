import copy

with open("C:\\Users\\perki\\Documents\\GitHub\\advent-of-code\\2024\\23\\Input\\input_test.txt", "r") as file:
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

    for n in nodes:
        print(n)
        print(connections[n])
        print()
    

    starter_nodes = copy.deepcopy(nodes)
    
    largest_clique = None
    largest_clique_size = 0
    while len(starter_nodes) > 0:
        print("remaining starter nodes: ")
        print(starter_nodes)
        print()
        clique = set(())
        start_node = starter_nodes[0]
        starter_nodes.remove(start_node)

        clique.add(start_node)
        remaining_nodes = copy.deepcopy(starter_nodes)
        print("start node:")
        print(start_node)
        print()
        
        for n1 in remaining_nodes:
            print("checking node " + str(n1))
            is_in_clique = True
            for n2 in clique:
                if n2 not in connections[n1]:
                    print("no connection found with node " + str(n2))
                    is_in_clique = False
                    break
            if is_in_clique:
                print("connection found with all nodes")
                remaining_nodes.remove(n1)
                clique.add(n1)
                print("new clique: " + str(clique))
            print()
        

        if len(clique) > largest_clique_size:
            print("new largest clique found")
            largest_clique_size = len(clique)
            largest_clique = copy.deepcopy(clique)
            print(largest_clique)
            print(largest_clique_size)
        print()


    print("largest clique:")
    print(largest_clique)
    print(largest_clique_size)