with open("C:\\Users\\perki\\Documents\\GitHub\\advent-of-code\\2024\\11\\Input\\input_test.txt", "r") as file:
    for line in file:
        input = line.rstrip("\n")
    
    stones = input.split(" ")
    print(stones)

    for i in range(6):
        new_stones = []
        for stone in stones:
            if stone == "0":
                new_stones.append("1")
            elif len(stone) % 2 == 0:
                stone_left = stone[:int((len(stone)/2))].lstrip("0")
                stone_right = stone[int(((len(stone)/2))):].lstrip("0")
                if stone_left == "":
                    stone_left = "0"
                if stone_right == "":
                    stone_right = "0"
                new_stones.append(stone_left)
                new_stones.append(stone_right)
            else:
                new_stones.append(str(int(stone)*2024))
        stones = new_stones
        print(stones)

