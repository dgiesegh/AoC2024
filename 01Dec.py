# -*- coding: utf-8 -*-

import _utils as u
import numpy as np

#Q1

lines = u.read_lines("01Dec.txt")

list_1 = np.array([int(lines[i].split("   ")[0]) for i in range(len(lines))])
list_2 = np.array([int(lines[i].split("   ")[1]) for i in range(len(lines))])

list_1.sort()
list_2.sort()
diff = np.abs(list_2 - list_1)

print("Q1 answer:", diff.sum())

#Q2

intersect = np.intersect1d(list_1, list_2)
occs = u.count_occurences(list_2, intersect, True)

print("Q2 answer:", (occs*intersect).sum())