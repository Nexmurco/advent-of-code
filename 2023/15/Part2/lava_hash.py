with open("D:\\Code\\Advent of Code 2023\\Dec15\\Part2\\input.txt", "r") as file:
    lines = list(file)
    instruction_line = lines[0]
    instruction_line = instruction_line.rstrip("\n")
    instructions = instruction_line.split(",")

    boxes = {}
    value_map = {}
    

    total = 0
    for i in instructions:
        command = None
        if "=" in i:
            command = "="
            key = i.split("=")[0]
            value = i.split("=")[1]
        elif "-" in i:
            command = "-"
            key = i.replace("-","")
        box_num = 0
        for char in key:
            box_num += ord(char)
            box_num *= 17
            box_num %= 256
        
        if command == "=":
            if box_num not in boxes.keys():
                boxes[box_num] = []
            if key not in boxes[box_num]:
                boxes[box_num].append(key)
            value_map[(box_num, key)] = value
        elif command == "-":
            if box_num in boxes.keys() and key in boxes[box_num]:
                boxes[box_num].remove(key)

    
    total = 0
    for box_key in boxes.keys():
        print("box " + str(box_key))
        for index in range(len(boxes[box_key])):
            key = boxes[box_key][index]
            value = value_map[(box_key, key)]
            score = (1+int(box_key)) * int(index+1) * int(value)
            print(key + ":" + value + " -> " + str(score))
            total += score
        print("---------------")
    print("total: " + str(total))


