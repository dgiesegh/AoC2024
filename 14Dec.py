# -*- coding: utf-8 -*-

import _utils as u
import numpy as np
import time

robots = u.read_lines("14Dec.txt")
XMAX = 101
YMAX = 103

pvs = []
for robot in robots:
    p, v = [a[2:] for a in robot.split(" ")]
    p = np.array([int(a) for a in p.split(",")])
    v = np.array([int(a) for a in v.split(",")])
    pvs.append([p,v])

end_locs = []
for pv in pvs:
    p, v = pv
    p_end = p + 100 * v
    p_end[0] -= int(p_end[0] / XMAX) * XMAX
    p_end[1] -= int(p_end[1] / YMAX) * YMAX
    if p_end[0] < 0:
        p_end[0] += XMAX
    if p_end[1] < 0:
        p_end[1] += YMAX
    end_locs.append(p_end)

score1 = 0
score2 = 0
score3 = 0
score4 = 0
for loc in end_locs:
    if loc[0] < int(XMAX/2) and loc[1] < int(YMAX/2):
        score1 += 1
    elif loc[0] < int(XMAX/2) and loc[1] > int(YMAX/2):
        score2 += 1
    elif loc[0] > int(XMAX/2) and loc[1] < int(YMAX/2):
        score3 += 1
    elif loc[0] > int(XMAX/2) and loc[1] > int(YMAX/2):
        score4 += 1

print("Q1 answer:", score1*score2*score3*score4)

def display_area(area):
    for line in area:
        for n in line:
            if n == 0:
                print(".", end="")
            else:
                print("X", end="")
        print()

i = 0
while True:
    area = np.zeros((XMAX, YMAX))
    for pv in pvs:
        p, v = pv
        p += v
        if p[0] < 0:
            p[0] += XMAX
        elif p[0] >= XMAX:
            p[0] -= XMAX
        if p[1] < 0:
            p[1] += YMAX
        elif p[1] >= YMAX:
            p[1] -= YMAX
        area[p[0], p[1]] += 1
    i += 1
    if (i-68)%101 == 0:
        print("\n Second:", i)
        display_area(area.T)
        input()

# Q2 answer: 7138