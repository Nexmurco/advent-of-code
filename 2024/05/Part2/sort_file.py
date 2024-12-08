with open("C:\\Users\\perki\\Documents\\GitHub\\advent-of-code\\2024\\05\\Input\\input.txt", "r") as file:
    commands = []
    for line in file:
        if line == "\n":
            break

        line = line.rstrip("\n")
        commands.append(line + "\n")
    
    commands.sort()

file1 = open("C:\\Users\\perki\\Documents\\GitHub\\advent-of-code\\2024\\05\\Input\\input_processed.txt", "w") 
file1.writelines(commands)
file1.close()
        
