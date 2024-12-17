# -*- coding: utf-8 -*-

import _utils as u

def check_xmas(matrix, coords):
    if coords[0] >= 1 and coords[1] >= 1 and coords[0] < len(matrix)-1 and coords[1] < len(matrix)-1:
        diag1 = matrix[coords[0]-1][coords[1]-1] + matrix[coords[0]+1][coords[1]+1]
        diag2 = matrix[coords[0]+1][coords[1]-1] + matrix[coords[0]-1][coords[1]+1]
        if diag1 in ["MS", "SM"] and diag2 in ["MS", "SM"]:
            return True
        return False

txt = u.read_lines("04Dec.txt")

#Q1

count = 0

coords = []
for l in range(len(txt)):
    line = txt[l]
    inds = u.find_substr(line, "X")
    for i in inds:
        coords.append([l,i])

for coord in coords:
    dirs = u.search_all_directions(txt, "M", coord)
    for d in dirs:
        if u.search_one_direction(txt, "MAS", coord, d):
            count += 1

print("Q1 answer:", count)

#Q2

count = 0

coords = []
for l in range(len(txt)):
    line = txt[l]
    inds = u.find_substr(line, "A")
    for i in inds:
        coords.append([l,i])

for c in coords:
    if check_xmas(txt, c):
        count += 1

print("Q2 answer:", count)