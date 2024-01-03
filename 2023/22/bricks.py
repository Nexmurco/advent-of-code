import copy

def brick_sort_bottom(b):
    return b["Z"][0]

def brick_sort_top(b):
    return b["Z"][1]

def interval_overlap(interval1, interval2):
    if interval1[1] < interval2[0] or interval1[0] > interval2[1]:
        return False
    return True



dimensions = ["X", "Y", "Z"]

bricks = []
with open("D:\\Code\\advent-of-code\\advent-of-code\\2023\\22\\input.txt", "r") as file:
    lines = list(file)
    id = 0
    for line in lines:
        line = line.rstrip("\n")
        coords = line.split("~")
        c1 = coords[0].split(",")
        c2 = coords[1].split(",")
        brick = {}
        brick["ID"] = id
        brick["X"] = (int(c1[0]), int(c2[0]))
        brick["Y"] = (int(c1[1]), int(c2[1]))
        brick["Z"] = (int(c1[2]), int(c2[2]))
        bricks.append(brick)
        id += 1

#sort brickes by their bottom z height

bricks.sort(key = brick_sort_bottom)


stable_bricks = []
stable_brick_map = {}
z_head_map = {}
z_butt_map = {}

for b in range(len(bricks)):
    brick = bricks[b]
#starting with the lowest brick, go toward the ground checking for collisions

    #try to lower the current brick checking for collisions with any bricks beneath it, working through them top to bottom
    fall_distance = brick["Z"][0] - 1
    for s in list(reversed(stable_bricks)):
        if interval_overlap(brick["X"], s["X"]) and interval_overlap(brick["Y"], s["Y"]):
            #set brick height to be 1 higher than the stable brick it has collided with
            fall_distance = brick["Z"][0] - (s["Z"][1] + 1)
            break

    butt = brick["Z"][0] - fall_distance
    head = brick["Z"][1] - fall_distance
    z_height = (butt, head)
    
    stable_brick = {"ID": brick["ID"], "X": brick["X"], "Y": brick["Y"], "Z":z_height}

    stable_bricks.append(stable_brick)
    stable_bricks.sort(key = brick_sort_top)
    stable_brick_map[brick["ID"]] = stable_brick

    if butt not in z_butt_map.keys():
        z_butt_map[butt] = []
    z_butt_map[butt].append(stable_brick["ID"])

    if head not in z_head_map.keys():
        z_head_map[head] = []
    z_head_map[head].append(stable_brick["ID"])


#add all above and below adjacencies to each brick
for s in stable_bricks:
    above = []
    below = []
    butt = s["Z"][0]
    head = s["Z"][1]

    head_check = butt - 1
    butt_check = head + 1

    if head_check in z_head_map.keys():
        for brick_key in z_head_map[head_check]:
            below_brick = stable_brick_map[brick_key]
            if interval_overlap(s["X"], below_brick["X"]) and interval_overlap(s["Y"], below_brick["Y"]):
                below.append(brick_key)

    if butt_check in z_butt_map.keys():
        for brick_key in z_butt_map[butt_check]:
            above_brick = stable_brick_map[brick_key]
            if interval_overlap(s["X"], above_brick["X"]) and interval_overlap(s["Y"], above_brick["Y"]):
                above.append(brick_key)
    
    s["below"] = below
    s["above"] = above
    #stable_bricks[s] = stable

#go through each brick, grab each above brick, and make sure it has more than 1 below brick, if this is true for every above brick, add 1
total = 0

for s in stable_bricks:
    safe_brick = True
    for a in s["above"]:
        above_brick = stable_brick_map[a]
        if len(above_brick["below"]) < 2:
            safe_brick = False
            break
    if safe_brick:
        s["safe"] = True
        total += 1
    else:
        s["safe"] = False

total_disruptions = 0

progress = 0
for stable in stable_bricks:
    progress += 1
    print(progress)

    adjust_brick_map = copy.deepcopy(stable_brick_map)
    adjust_brick_map[stable["ID"]]["disturbed"] = True
    disturb_queue = []
    #add all bricks directly our starting brick to the queue
    for a in stable["above"]:
        above_brick = adjust_brick_map[a]
        disturb_queue.append((above_brick["Z"][0], above_brick["ID"]))

    disturbed_bricks = set()

    while len(disturb_queue) > 0:
        #sort disturbed bricks by z butt height, so we go bottom to top
        disturb_queue.sort()

        cur_brick = adjust_brick_map[disturb_queue.pop(0)[1]]

        #if all bricks below this one are disturbed, then it is also disturbed
        disturb = True
        for below in cur_brick["below"]:
            below_brick = adjust_brick_map[below]
            if "disturbed" not in below_brick.keys() or below_brick["disturbed"] == False:
                disturb = False
                break
        cur_brick["disturbed"] = disturb

        #if disturbed, add all bricks directly above
        if disturb:
            disturbed_bricks.add(cur_brick["ID"])
            for a in cur_brick["above"]:
                above_brick = adjust_brick_map[a]
                disturb_queue.append((above_brick["Z"][0], above_brick["ID"]))
    
    disturb_count = len(disturbed_bricks)
    total_disruptions += disturb_count

print()
print(total)
print(total_disruptions)