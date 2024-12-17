# -*- coding: utf-8 -*-

import _utils as u

def try_all_combos(total, nums, test_concat=False):
    if len(nums) == 1:
        return nums[0] == total
    num = nums[0]
    newnums1 = [nums[i] for i in range(1, len(nums))]
    newnums2 = newnums1.copy()
    newnums3 = newnums1.copy()
    newnums1[0] += num
    match = try_all_combos(total, newnums1, test_concat)
    if match:
        return True
    newnums2[0] *= num
    match = try_all_combos(total, newnums2, test_concat)
    if match:
        return True
    if test_concat:
        newnums3[0] = int(str(num)+str(newnums3[0]))
        match = try_all_combos(total, newnums3, test_concat)
        if match:
            return True
    return False

lines = u.read_lines("07Dec.txt")

totals = []
numbers = []
for line in lines:
    tot, nums = line.split(": ")
    nums = [int(a) for a in nums.split(" ")]
    tot = int(tot)
    totals.append(tot)
    numbers.append(nums)

score1 = 0
for i in range(len(totals)):
    total = totals[i]
    nums = numbers[i]
    if try_all_combos(total, nums):
        score1 += total

score2 = 0
for i in range(len(totals)):
    total = totals[i]
    nums = numbers[i]
    if try_all_combos(total, nums, True):
        score2 += total

print("Q1 answer:", score1)
print("Q2 answer:", score2)