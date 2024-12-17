# -*- coding: utf-8 -*-

import _utils as u
import numpy as np

def find_start(matrix):
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if lab[i,j] == "^":
                return [i,j]

def print_board(matrix):
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            print(matrix[i,j], end="")
        print()

def find_path_length(matrix, start, direction):
    directions = {"[-1, 0]": [0, 1], "[0, 1]": [1, 0], "[1, 0]": [0, -1], "[0, -1]": [-1, 0]}
    
    i, j = start
    positions = []
    while i >= 0 and i < matrix.shape[0] and j >= 0 and j < matrix.shape[1]:
        #print(i, j, direction)
        if matrix[i, j] == "#":
            i -= direction[0]
            j -= direction[1]
            direction = directions[str(direction)]
        if hash(str([i,j])+str(direction)) in positions:
            print("LOOP!")
            return None, None, True
        positions.append(hash(str([i,j])+str(direction)))
        matrix[i, j] = "X"
        i += direction[0]
        j += direction[1]
    count = 0
    positions = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if matrix[i,j] == "X":
                count += 1
                if i != start[0] or j != start[1]:
                    positions.append([i,j])
    return count, positions, False

lab = u.read_lines("06Dec.txt")
lab = u.make_matrix_from_readlines(lab)

#Q1

start = find_start(lab)
direction = [-1, 0]
count, positions, _ = find_path_length(np.copy(lab), start, direction)

print("Q1 answer:", count)

#Q2

count = 0
for i in range(len(positions)):
    pos = positions[i]
    print("Pos", i+1, "of", len(positions), "count is", count)
    lab[pos[0], pos[1]] = "#"
    c, p, loop = find_path_length(np.copy(lab), start, direction)
    lab[pos[0], pos[1]] = ".";
    if loop:
        count += 1

print("Q2 answer:", count)