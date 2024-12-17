# -*- coding: utf-8 -*-

import _utils as u

lines = u.read_lines("13Dec.txt")

machines = []

for i in range(int(len(lines)/4)):
    numbers = []
    for j in range(4):
        line = lines[4*i+j]
        if j != 3:
            line = line[10:] if j == 0 or j == 1 else line[7:]
            nums = [int(n[2:]) for n in line.split(", ")]
            for n in nums:
                numbers.append(n)
    machines.append(numbers)

scores = []
scores2 = []

for machine in machines:
    
    a = (machine[3] * machine[4] - machine[2] * machine[5]) / (machine[0] * machine[3] - machine[2] * machine[1])
    b = (machine[5] - a * machine[1]) / machine[3]
    if abs(int(a) - a) < 0.001 and abs(int(b) - b) < 0.001:
        scores.append(int(3*a+b))
    else:
        scores.append(0)
    
    machine[4] += 10000000000000
    machine[5] += 10000000000000
    a = (machine[3] * machine[4] - machine[2] * machine[5]) / (machine[0] * machine[3] - machine[2] * machine[1])
    b = (machine[5] - a * machine[1]) / machine[3]
    if abs(int(a) - a) < 0.001 and abs(int(b) - b) < 0.001:
        scores2.append(int(3*a+b))
    else:
        scores2.append(0)

print("Q1 answer:", sum(scores))
print("Q2 answer:", sum(scores2))