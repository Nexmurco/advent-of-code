import re
import math

count_map = {}

def count(arr, nums):
    #if we have run out of numbers, increase our count by 1, unless there are required spaces that were missed
    if len(nums) == 0:
        if "#" in arr:
            count_map[(arr, nums)] = 0
            return 0
        else:
            count_map[(arr, nums)] = 1
            return 1
        
    #if there are not enough positions left to continue, return 0
    needed_length = 0
    for n in nums:
        needed_length += n
    needed_length += len(nums) - 1

    if needed_length > len(arr):
        count_map[(arr, nums)] = 0
        return 0
    
    #check if this is a pattern we have already encountered, if so use, use the precalculated value
    if (arr, nums) in count_map.keys():
        return count_map[(arr, nums)]
    
    #this is a setup we have not encountered before, so calculate the new value
    num = nums[0]
    sum = 0

    start_substring = arr[:num]
    if num > len(arr) - 1:
        buffer_space = ""
    else:
        buffer_space = arr[num]

    #if we start with a period, or our buffer space is a #, skip this iteration
    if "." in start_substring or buffer_space == "#":
        if arr[0] == "#":
            sum = 0
        else:
            sum += count(arr[1:], nums)
        count_map[(arr, nums)] = sum
        return sum

    else:
        sum += count(arr[num+1:], nums[1:])
        #if we pass a required space, end, otherwise see if there are additional fits to the right
        if arr[0] != "#":
            sum += count(arr[1:], nums)

    
    count_map[(arr, nums)] = sum
    return sum
        
    

def increasing_permutations(s, v):
    product = 1
    if s == 0 or v == 0:
        return product
    for i in range(s):
        product *= (v + i)
    product //= math.factorial(s)
    return product

def character_match(char1, char2):
    if char1 == char2:
        return True
    elif char1 == "?" and (char2 == "." or char2 == "#"):
        return True
    elif char2 == "?" and (char1 == "." or char1 == "#"):
        return True
    return False

total_arrangements = 0

fout = open(".\\Dec12\\Part2-B\\output-B.txt", "w")

with open("D:\\Code\\Advent of Code 2023\\Dec12\\Part2-B\\input.txt", "r") as file:
    lines = list(file)
    it = 0
    for line in lines:
        it += 1
        line = line.rstrip("\n")
        line_split = line.split(" ")
        
        data_arrangement = line_split[0]
        data_numeric = tuple([int(num) for num in line_split[1].split(",")])

        arr = data_arrangement+"?"+data_arrangement+"?"+data_arrangement+"?"+data_arrangement+"?"+data_arrangement
        nums = data_numeric+data_numeric+data_numeric+data_numeric+data_numeric
        print(arr)
        print(nums)

        arrangements = count(arr, nums)
        print(arrangements, file=fout)
        print(str(it) + ": " + str(arrangements))
        total_arrangements += arrangements
        print()
    
    print("----------------------")
    print(total_arrangements)

fout.close()
    






  

