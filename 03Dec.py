# -*- coding: utf-8 -*-

import _utils as u

def parse_mul(string, index):
    if string[index:index+4] != "mul(":
        return -1
    index += 4
    num1 = ""
    while u.is_numeric(string[index]):
        num1 += string[index]
        index += 1
    if string[index] != ",":
        return -1
    index += 1
    num2 = ""
    while u.is_numeric(string[index]):
        num2 += string[index]
        index += 1
    if string[index] != ")":
        return -1
    try:
        return int(num1) * int(num2)
    except:
        return -1

memory_l = u.read_lines("03Dec.txt")
memory = ""
for m in memory_l:
    memory += m

#Q1

res = 0
occ = u.find_substr(memory, "mul(")
for i in occ:
    a = parse_mul(memory, i)
    if a != -1:
        res += a

print("Q1 answer:", res)

#Q2

occ_d = u.find_substr(memory, "do()")
occ_dt = u.find_substr(memory, "don't()")
memory_clean = memory

for i in occ_dt:
    found = False
    for j in occ_d:
        if j > i:
            found = True
            memory_clean = memory_clean[:i] + "X"*(j-i) + memory_clean[j:]
            break
    if not found:
        memory_clean = memory_clean[:i] + "X"*(len(memory_clean)-i)

res = 0
occ = u.find_substr(memory_clean, "mul(")
for i in occ:
    a = parse_mul(memory_clean, i)
    if a != -1:
        res += a

print("Q2 answer:", res)