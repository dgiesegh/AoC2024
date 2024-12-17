# -*- coding: utf-8 -*-

import numpy as np
import _utils as u

def find_last_num_and_first_space(disk, start, stop):
    first = 0
    last = 0
    for i in range(start, len(disk)):
        if disk[i] == -1:
            first = i
            break
    for i in range(stop, -1, -1):
        if disk[i] != -1:
            last = i
            return first, last

def find_last_block(disk, stop):
    found = False
    num = 0
    length = 0
    index = 0
    for i in range(stop, -1, -1):
        if not found and disk[i] != -1:
            num = disk[i]
            length += 1
            found = True
        elif found and disk[i] != num:
            index = i+1
            break
        elif found:
            length += 1
    return index, num, length

def find_first_space_with_length(disk, length, stop):
    space = False
    s_length = 0
    for i in range(stop):
        if disk[i] == -1:
            s_length += 1
            if s_length >= length:
                return i-s_length+1
        else:
            s_length = 0
    return -1

#with open("09Dec.txt") as file:
#    disk_code = file.readline()
disk_code = u.read_lines("09Dec.txt")[0]

total_length = sum([int(i) for i in disk_code])
index = 0
disk = np.zeros(total_length)
for i in range(len(disk_code)):
    if i % 2 == 0:
        for j in range(int(disk_code[i])):
            disk[index] = int(i/2+0.1)
            index += 1
    else:
        for j in range(int(disk_code[i])):
            disk[index] = -1
            index += 1

#Q1

working_disk = disk.copy()
curr_max = len(disk)-1
curr_min = 0
while True:
    first, last = find_last_num_and_first_space(working_disk, curr_min, curr_max)
    curr_max = last
    curr_min = first
    print("First", first, "last", last)
    if last < first:
        break
    working_disk[first] = working_disk[last]
    working_disk[last] = -1

score = 0
for i in range(len(working_disk)):
    if working_disk[i] != -1:
        score += working_disk[i] * i

print("Q1 answer:", score)

#Q2

working_disk = disk.copy()
curr_max = len(working_disk)-1
while True:
    index, num, length = find_last_block(working_disk, curr_max)
    if index == 0:
        break
    curr_max = index-1
    space_index = find_first_space_with_length(working_disk, length, index)
    print("Index", index, "space index", space_index)
    if space_index != -1 and space_index < index:
        for i in range(length):
            working_disk[index+i] = -1
            working_disk[space_index+i] = num

score = 0
for i in range(len(working_disk)):
    if working_disk[i] != -1:
        score += working_disk[i] * i

print("Q2 answer:", score)