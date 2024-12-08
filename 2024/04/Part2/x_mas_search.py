
with open("C:\\Users\\perki\\Documents\\GitHub\\advent-of-code\\2024\\04\\Input\\input_test.txt", "r") as file:
    
    sum = 0

    lines = []
    for line in file:
        line = line.rstrip("\n")
        lines.append(line)

    letter_arrangements = ["MMASS", "MSAMS", "SMASM", "SSAMM"]

    for i in range(len(lines)-2):
        line = lines[i]
        for j in range(len(line)-2):
            #there are only 4 configurations
            #M.M***M.S***S.M***S.S
            #.A.***.A.***.A.***.A.
            #S.S***M.S***S.M***M.M
            #reading like a book the arrangements are:
            #MMASS
            #MSAMS
            #SMASM
            #SSAMM
            letters = ""
            letters += lines[i][j]
            letters += lines[i][j+2]
            letters += lines[i+1][j+1]
            letters += lines[i+2][j]
            letters += lines[i+2][j+2]
            if letters in letter_arrangements:
                sum += 1
                print("Found arrangement " + letters + " at pos " + str((j,i)))




            


    print("-----------")
    print("sum: " + str(sum))