# -*- coding: utf-8 -*-

import _utils as u
import numpy as np

lines = u.read_lines("05Dec.txt")
orders = None
page_lists = None
for i in range(len(lines)):
    if lines[i] == "":
        orders = [lines[j] for j in range(i)]
        page_lists = [lines[j] for j in range(i+1,len(lines))]
        break

order_graph = u.Graph()
for order in orders:
    ids = [int(a) for a in order.split("|")]
    if not order_graph.exists_node(ids[1]):
        order_graph.add_node(ids[1], [], False)
    if not order_graph.exists_node(ids[0]):
        order_graph.add_node(ids[0], [ids[1]], False)
    else:
        order_graph.add_connection(ids[0], ids[1], False)

score = 0
incorrect_sorting_score = 0
for pages in page_lists:
    nums = [int(a) for a in pages.split(",")]
    correct = True
    for i in range(len(nums)-1):
        if not order_graph.exists_connection(nums[i], nums[i+1]):
            correct = False
            break
    if correct:
        score += nums[int(len(nums)/2)]
        print(nums, "is CORRECTLY sorted")
    else:
        nums_sorted = [0]*len(nums)
        for num in nums:
            nextnums = np.intersect1d(order_graph.get_neighbours(num), nums)
            nums_sorted[len(nums)-1-len(nextnums)] = num
        incorrect_sorting_score += nums_sorted[int(len(nums)/2)]
        print(nums, "is INCORRECTLY sorted, correct version is", nums_sorted)

print("Q1 answer is", score)
print("Q2 answer is", incorrect_sorting_score)