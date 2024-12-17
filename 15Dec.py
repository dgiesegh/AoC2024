# -*- coding: utf-8 -*-

import _utils as u
import numpy as np

def print_board(board):
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            print(board[i,j], end="")
        print()

lines = u.read_lines("15Dec.txt")

house = []
instructions = ""
empty_line_found = False
for line in lines:
    if line == "":
        empty_line_found = True
    elif empty_line_found:
        instructions += line
    else:
        house.append(line)

house = u.make_matrix_from_readlines(house)
house_copy = house.copy()
instructions = list(instructions)

robot_pos = None
for i in range(house.shape[0]):
    for j in range(house.shape[1]):
        if house[i,j] == "@":
            robot_pos = np.array([i,j])


directions = {">":np.array([0,1]), "<":np.array([0,-1]), 
              "^":np.array([-1,0]), "v":np.array([1,0])}
for i in range(len(instructions)):
    cmd = instructions[i]
    direction = directions[cmd]
    move = False
    last_box = None
    ray_pos = robot_pos.copy()
    while True:
        ray_pos += direction
        if house[ray_pos[0], ray_pos[1]] == "#":
            break
        elif house[ray_pos[0], ray_pos[1]] == ".":
            move = True
            break
        elif house[ray_pos[0], ray_pos[1]] == "O":
            last_box = ray_pos.copy()
    if move:
        if last_box is not None:
            pos = last_box + direction
            house[pos[0], pos[1]] = "O"
        house[robot_pos[0], robot_pos[1]] = "."
        robot_pos += direction
        house[robot_pos[0], robot_pos[1]] = "@"

score = 0
for i in range(house.shape[0]):
    for j in range(house.shape[1]):
        if house[i,j] == "O":
            score += 100 * i + j

print("Q1 answer:", score)

house2 = np.empty([house.shape[0], 2*house.shape[1]], dtype=str)
for i in range(house.shape[0]):
    for j in range(house.shape[1]):
        if house_copy[i,j] == "#":
            house2[i,2*j] = "#"
            house2[i,2*j+1] = "#"
        elif house_copy[i,j] == ".":
            house2[i,2*j] = "."
            house2[i,2*j+1] = "."
        elif house_copy[i,j] == "O":
            house2[i,2*j] = "["
            house2[i,2*j+1] = "]"
        elif house_copy[i,j] == "@":
            house2[i,2*j] = "@"
            house2[i,2*j+1] = "."

robot_pos = None
for i in range(house2.shape[0]):
    for j in range(house2.shape[1]):
        if house2[i,j] == "@":
            robot_pos = np.array([i,j])

for i in range(len(instructions)):
    cmd = instructions[i]
    direction = directions[cmd]
    if direction[1] != 0:
        move = False
        ray_pos = robot_pos.copy()
        while True:
            ray_pos += direction
            if house2[ray_pos[0], ray_pos[1]] == "#":
                break
            elif house2[ray_pos[0], ray_pos[1]] == ".":
                move = True
                break
        if move:
            house2[robot_pos[0], robot_pos[1]+direction[1]:ray_pos[1]+direction[1]:direction[1]] = house2[robot_pos[0], robot_pos[1]:ray_pos[1]:direction[1]]
            house2[robot_pos[0], robot_pos[1]] = "."
            robot_pos += direction
    else:
        check_positions = [robot_pos+direction]
        move = True
        boxes = []
        while len(check_positions) != 0:
            pos = check_positions.pop(0)
            c = house2[pos[0], pos[1]]
            if c=="#":
                move = False
                break
            elif c=="[":
                check_positions.append(pos+direction)
                check_positions.append(pos+direction+np.array([0,1]))
                boxes.append(pos)
            elif c=="]":
                check_positions.append(pos+np.array([0,-1]))
        if move:
            for box in boxes[::-1]:
                house2[box[0], box[1]] = "."
                house2[box[0], box[1]+1] = "."
                house2[box[0]+direction[0], box[1]] = "["
                house2[box[0]+direction[0], box[1]+1] = "]"
            house2[robot_pos[0], robot_pos[1]] = "."
            robot_pos += direction
            house2[robot_pos[0], robot_pos[1]] = "@"

score = 0
for i in range(house2.shape[0]):
    for j in range(house2.shape[1]):
        if house2[i,j] == "[":
            score += 100 * i + j
print("Q2 answer:", score)