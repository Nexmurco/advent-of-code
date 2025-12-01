import copy
def bron_kerbosh(set_r, set_p, set_x):
    global connections


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

    
    
