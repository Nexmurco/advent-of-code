from functools import cmp_to_key


# Card Hand Ranks
# 5 of kind 6
# 4 of kind 5
# full house 4
# 3 of kind 3
# 2 pair 2
# 1 pair 1
# high card 0

cardValueMap = {
    "2":0,
    "3":1,
    "4":2,
    "5":3,
    "6":4,
    "7":5,
    "8":6,
    "9":7,
    "T":8,
    "J":9,
    "Q":10,
    "K":11,
    "A":12,
}


def handTypeCompare(hand1, hand2):
    for i in range(5):
        if cardValueMap[hand1["hand"][i]] > cardValueMap[hand2["hand"][i]]:
            return 1
        elif cardValueMap[hand1["hand"][i]] < cardValueMap[hand2["hand"][i]]:
            return -1
    
    return 0

def handType(hand):
    #make of map with letters as the key and count as the value
    charCountMap = {}
    kindCountMap = {1:0,2:0,3:0,4:0,5:0}
    for char in list(hand):
        if char not in charCountMap.keys():
            charCountMap[char] = 0

        charCountMap[char] += 1
    
    for count in charCountMap.values():
        kindCountMap[count] += 1

    #check for five of a kind
    if kindCountMap[5] >= 1:
        return 6
    elif kindCountMap[4] >= 1:
        return 5
    elif kindCountMap[3] >= 1 and kindCountMap[2] >= 1:
        return 4
    elif kindCountMap[3] >= 1:
        return 3
    elif kindCountMap[2] >= 2:
        return 2
    elif kindCountMap[2] >= 1:
        return 1
    
    return 0


with open("D:\\Code\\Advent of Code 2023\\Dec07\\Part1\\input.txt", "r") as file:

    lines = list(file)
    handsByType = {0:[],1:[],2:[],3:[],4:[],5:[],6:[]}
    for line in lines:
        line = line.rstrip("\n")
        data = line.split(" ")
        hand = data[0]
        bid = data[1]
        #print("hand: " + hand + ", bid: " + bid)
        handMapData = {}
        handMapData["hand"] = hand
        handMapData["bid"] = bid
        handMapData["handtype"] = handType(hand)
        #print(handMapData)
        handsByType[handMapData["handtype"]].append(handMapData)

    total_hands = 0
    for t in handsByType.keys():
        total_hands += len(handsByType[t])
        handsByType[t] = sorted(handsByType[t], key=cmp_to_key(handTypeCompare))
    
    total_winnings = 0
    rank = 0
    for t in handsByType:
        for h in handsByType[t]:
            print(h)
            rank += 1
            winnings = rank * int(h["bid"])
            print(str(total_winnings) + " + (" + h["bid"] + " * " + str(rank) + ")")
            total_winnings += winnings
            print(total_winnings)
            print()

    print(total_winnings)



