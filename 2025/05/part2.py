import sys
input_file = sys.argv[1]


def is_overlapping(interval1, interval2):
    if interval1 is None or interval2 is None:
        return False
    if (interval1[1] < interval2[0]) or (interval2[1] < interval1[0]):
        return False
    return True

def combine_intervals(interval1, interval2):
    new_interval = (min(interval1[0], interval2[0]), max(interval1[1], interval2[1]))
    return new_interval


intervals = []

with open(input_file, "r") as input_lines:
    for input in input_lines:
        line = input.rstrip()
        if line == '':
            break
        line = line.split('-')
        intervals.append((int(line[0]), int(line[1])))

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

count = 0

for interval in merged_intervals:
    count += (interval[1] - interval[0]) + 1
print(count)