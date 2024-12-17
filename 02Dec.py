# -*- coding: utf-8 -*-

import _utils as u

# returns index at which unsafety occurs
def test_safety(nums):
    if nums[1]-nums[0] == 0:
        return 0
    sign = (nums[1]-nums[0]) / abs(nums[1]-nums[0])
    for i in range(len(nums)-1):
        diff = nums[i+1] - nums[i]
        if abs(diff) < 1 or abs(diff) > 3 or diff * sign < 0:
            return i
    return -1


reports = u.read_lines("02Dec.txt")

#Q1

safe_reports = 0
unsafe_reports = 0

for report in reports:
    nums = [int(a) for a in report.split(" ")]
    i = test_safety(nums)
    if i == -1:
        safe_reports += 1
    else:
        unsafe_reports += 1

print("Q1 answer:", safe_reports, unsafe_reports)

#Q2

safe_reports = 0
unsafe_reports = 0

for report in reports:
    nums = [int(a) for a in report.split(" ")]
    i = test_safety(nums)
    if i == -1:
        safe_reports += 1
        continue
    j = test_safety([nums[a] for a in range(len(nums)) if a != i-1])
    if j == -1:
        safe_reports += 1
        continue
    j = test_safety([nums[a] for a in range(len(nums)) if a != i])
    if j == -1:
        safe_reports += 1
        continue
    j = test_safety([nums[a] for a in range(len(nums)) if a != i+1])
    if j == -1:
        safe_reports += 1
    else:
        unsafe_reports += 1
    

print("Q2 answer:", safe_reports, unsafe_reports)
