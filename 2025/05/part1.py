import sys
input_file = sys.argv[1]


def is_overlapping(interval1, interval2):
    if interval1 is None or interval2 is None:
        return False
    if interval1[1] < interval2[0] or interval2[1] < interval1[1]:
        return False
    return True

def combine_intervals(interval1, interval2):
    new_interval = (min(interval1[0], interval2[0]), max(interval1[1], interval2[1]))
    return new_interval


intervals = []
ids = []
input_part1 = True

with open(input_file, "r") as input_lines:
    for input in input_lines:
        line = input.rstrip()
        if input_part1:
            if line == '':
                input_part1 = False
                continue
            line = line.split('-')
            intervals.append((int(line[0]), int(line[1])))
        else:
            ids.append(int(line))


#print(intervals)
#print(ids)

intervals.sort()

merged_intervals = []


prev = None
for i in iter(intervals):
    if is_overlapping(prev, i):
        prev = combine_intervals(prev, i)
    elif prev is not None:
        merged_intervals.append(prev)
        prev = i
    else:
        prev = i
merged_intervals.append(prev)


interval_list = []
interval_map = {}
interval_list.append(-1)
interval_map[-1] = False
for interval in merged_intervals:
    l = interval[0]
    r = interval[1] + 1
    interval_map[l] = True
    interval_map[r] = False
    interval_list.append(l)
    interval_list.append(r)

true_count = 0
for id in ids:
    prev = -1
    for i in interval_list:
        if id < i:
            break
        prev = i
    if interval_map[prev] is True:
        true_count += 1
    
print(true_count)