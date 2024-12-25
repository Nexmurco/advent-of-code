def mix(num1, num2):
    return num1 ^ num2

def prune(num):
    return num % 16777216

def next_secret(secret):
    val1 = secret
    val2 = val1 * 64
    # print(str(val1) + " * 64 = " + str(val2))
    val1 = mix(secret, (secret * 64))
    # print("mix: " + str(val1))
    val1 = prune(val1)
    # print("prune: " + str(val1))

    val2 = int(val1 / 32)
    # print(str(val1) + " / 32 = " + str(val2))
    val1 = mix(val1, val2)
    # print("mix: " + str(val1))
    val1 = prune(val1)
    # print("prune: " + str(val1))

    val2 = val1 * 2048
    # print(str(val1) + " * 2048 = " + str(val2))
    val1 = mix(val1, val2)
    # print("mix: " + str(val1))
    val1 = prune(val1)
    # print("prune: " + str(val1))
    return val1


with open("C:\\Users\\perki\\Documents\\GitHub\\advent-of-code\\2024\\22\\Input\\input_test2.txt", "r") as file:
    seller_id = 0
    seller_map = {}

    for line in file:
        sequence_map = {}
        seller_map[seller_id] = sequence_map
        secret = int(line.rstrip("\n"))
        price = secret % 10
        
        change_list = []
        for i in range(2000):
            prev_price = price
            secret = next_secret(secret)
            price = secret % 10
            change = price - prev_price

            change_list.append(change)

            if len(change_list) == 4:
                sequence = (change_list[0], change_list[1], change_list[2], change_list[3])
                if sequence not in sequence_map:
                    sequence_map[sequence] = price
                elif price > sequence_map[sequence]:
                    sequence_map[sequence] = price
                change_list.pop(0)
            
        seller_id += 1

    value_map = {}
    
    highest_value = 0
    highest_sequence = None

    for key in seller_map:
        # print("seller #" + str(key))
        for key2 in seller_map[key]:
            # print(str(key2) + ": " + str(seller_map[key][key2]))
            if key2 not in value_map:
                value_map[key2] = 0
            
            value_map[key2] += seller_map[key][key2]

            if value_map[key2] > highest_value:
                highest_value = value_map[key2]
                highest_sequence = key2

    print("sequence: " + str(highest_sequence))
    print("bananas bananned: " + str(highest_value))