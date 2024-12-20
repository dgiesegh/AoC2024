# -*- coding: utf-8 -*-

import _utils as u

def dfs(design, patterns, ptr=0):
    if ptr == len(design):
        return True
    for p in patterns:
        if p == design[ptr:ptr+len(p)]:
            if dfs(design, patterns, ptr+len(p)):
                return True
    return False

def dfs2(design, patterns, ptr=0, hashmap={}):
    if ptr == len(design):
        return 1
    if hash(design[ptr:]) in hashmap.keys():
        return hashmap[hash(design[ptr:])]
    score = 0
    for p in patterns:
        if p == design[ptr:ptr+len(p)]:
            score += dfs2(design, patterns, ptr+len(p), hashmap)
    hashmap[hash(design[ptr:])] = score
    return score

lines = u.read_lines("19Dec.txt")

patterns = lines[0].split(", ")
designs = lines[2:]

possible = 0
for design in designs:
    if dfs(design, patterns, 0):
        possible += 1

print("Q1 answer:", possible)

score = 0
hashmap = {}
for design in designs:
    score += dfs2(design, patterns, 0, hashmap)

print("Q2 anwer:", score)