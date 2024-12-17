# -*- coding: utf-8 -*-

import _utils as u

def display_maze(maze, graph1=[], graph2=[]):
    for i in range(maze.shape[0]):
        for j in range(maze.shape[1]):
            if [i,j] in graph1:
                print("*", end="")
            elif [i,j] in graph2:
                print("+", end="")
            else:
                print(maze[i,j], end="")
        print()

maze = u.make_matrix_from_readlines(u.read_lines("16Dec.txt"))

start_pos = [maze.shape[0]-2, 1]
end_pos = [1, maze.shape[1]-2]
maze[end_pos[0], end_pos[1]] = "."

left_turns = {"[1, 0]":[0, 1], "[0, 1]":[-1, 0], "[-1, 0]":[0, -1], "[0, -1]":[1, 0]}
right_turns = {"[1, 0]":[0, -1], "[0, 1]":[1, 0], "[-1, 0]":[0, 1], "[0, -1]":[-1, 0]}

seekers = []
seekers.append([start_pos, [0, 1], 0, []])
visited = {}
histories = {}
final_score = 1000000
best_paths = []
while len(seekers) > 0:
    seekers.sort(key = lambda s: s[2])
    pos, direc, dist, hist = seekers.pop(0)
    hist.append(pos.copy())
    if hash(str(pos)+str(direc)) in visited.keys() and visited[hash(str(pos)+str(direc))]<dist:
        continue
    if pos == end_pos:
        if dist <= final_score:
            final_score = dist
            best_paths += hist
    visited[hash(str(pos)+str(direc))] = dist
    histories[hash(str(pos)+str(direc))] = hist.copy()
    l_dir = left_turns[str(direc)]
    r_dir = right_turns[str(direc)]
    if maze[pos[0]+l_dir[0], pos[1]+l_dir[1]] == ".":
        seekers.append([[pos[0]+l_dir[0], pos[1]+l_dir[1]], l_dir, dist+1001, hist.copy()])
    if maze[pos[0]+r_dir[0], pos[1]+r_dir[1]] == ".":
        seekers.append([[pos[0]+r_dir[0], pos[1]+r_dir[1]], r_dir, dist+1001, hist.copy()])
    pos = [pos[0]+direc[0], pos[1]+direc[1]]
    if maze[pos[0], pos[1]] == ".":
        seekers.append([pos, direc, dist+1, hist])

print("Q1 answer:", final_score)
print("Q2 answer:", len(set([str(a) for a in best_paths])))
