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


with open("C:\\Users\\perki\\Documents\\GitHub\\advent-of-code\\2024\\22\\Input\\input.txt", "r") as file:
    sum = 0
    for line in file:
        secret = int(line.rstrip("\n"))
        for i in range(2000):
            secret = next_secret(secret)
        sum += secret
    print("sum: " + str(sum))