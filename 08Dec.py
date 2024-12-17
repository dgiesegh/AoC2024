# -*- coding: utf-8 -*-

import _utils as u
import numpy as np

def in_boundaries(node, city):
    return node[0] >= 0 and node[1] >= 0 and node[0] < city.shape[0] and node[1] < city.shape[1]

city = u.read_lines("08Dec.txt")
city = u.make_matrix_from_readlines(city)

positions = {}
for i in range(city.shape[0]):
    for j in range(city.shape[1]):
        loc = city[i,j]
        if loc != ".":
            if loc in positions.keys():
                positions[loc].append(np.array([i,j]))
            else:
                positions[loc] = [np.array([i,j])]

#Q1

score = 0
for k in positions.keys():
    for i in range(len(positions[k])):
        for j in range(i+1, len(positions[k])):
            pos1 = positions[k][i]
            pos2 = positions[k][j]
            diff = pos2 - pos1
            node1 = pos1 - diff
            node2 = pos2 + diff
            if in_boundaries(node1, city) and city[node1[0], node1[1]] != "#":
                score += 1
                city[node1[0], node1[1]] = "#"
            if in_boundaries(node2, city) and city[node2[0], node2[1]] != "#":
                score += 1
                city[node2[0], node2[1]] = "#"

print("Q1 answer:", score)

#Q2

city = u.read_lines("08Dec.txt")
city = u.make_matrix_from_readlines(city)

score = 0
for k in positions.keys():
    for i in range(len(positions[k])):
        for j in range(i+1, len(positions[k])):
            pos1 = positions[k][i]
            pos2 = positions[k][j]
            diff = pos2 - pos1
            node1 = pos1.copy()
            while in_boundaries(node1, city):
                if city[node1[0], node1[1]] != "#":
                    score += 1
                    city[node1[0], node1[1]] = "#"
                node1 -= diff
            node2 = pos2.copy()
            while in_boundaries(node2, city):
                if city[node2[0], node2[1]] != "#":
                    score += 1
                    city[node2[0], node2[1]] = "#"
                node2 += diff

print("Q2 answer:", score)