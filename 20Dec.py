# -*- coding: utf-8 -*-

import _utils as u

def build_graph(grid):
    graph = u.Graph()
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i,j] in [".", "S", "E"]:
                graph.add_node(hash(str([i,j])), {"pos":[i,j]}, [])
                if grid[i-1,j] in [".", "S", "E"]:
                    graph.add_connection(hash(str([i,j])), hash(str([i-1,j])))
                if grid[i,j-1] in [".", "S", "E"]:
                    graph.add_connection(hash(str([i,j])), hash(str([i,j-1])))
    return graph

maze = u.make_matrix_from_readlines(u.read_lines("20Dec.txt"))

graph = build_graph(maze)

end = None
start = None
for i in range(maze.shape[0]):
    for j in range(maze.shape[1]):
        if maze[i,j] == "E":
            end = [i,j]
        elif maze[i,j] == "S":
            start = [i,j]

# Dijkstra is technically unnecessary, but I realized too late there is only one path, and this works too
u.dijkstra(graph, hash(str(end)), 0, 100000000, lambda n1,n2: 1, "distance", "prev")
print("dijkstra 1 done")
u.dijkstra(graph, hash(str(start)), 0, 100000000, lambda n1,n2: 1, "distance2", "prev2")
print("dijkstra 2 done")
vanilla_dist = graph.nodes[hash(str(end))].properties["distance2"]

# Q1

directions = [[0,1], [1,0], [-1,0], [0,-1]]
shortcuts = []
for i in range(maze.shape[0]):
    for j in range(maze.shape[1]):
        if maze[i,j] in [".", "S"]:
            dist2 = graph.nodes[hash(str([i,j]))].properties["distance2"]
            for dir in directions:
                try:
                    if maze[i+dir[0], j+dir[1]] == "#" and maze[i+2*dir[0], j+2*dir[1]] in [".", "E"]:
                        total_dist = dist2 + graph.nodes[hash(str([i+2*dir[0], j+2*dir[1]]))].properties["distance"] + 2
                        if total_dist < vanilla_dist:
                            shortcuts.append(vanilla_dist-total_dist)
                except:
                    pass

score = 0
for s in shortcuts:
    if s >= 100:
        score += 1
print("Q1 answer:", score)

# Q2

shortcuts = {}
for i in range(maze.shape[0]):
    for j in range(maze.shape[1]):
        if maze[i,j] in [".", "S"]:
            dist2 = graph.nodes[hash(str([i,j]))].properties["distance2"]
            for a in range(-20, 21):
                for b in range(-20+abs(a), 21-abs(a)):
                    try:
                        if maze[i+a, b+j] in [".", "E"]:
                            dist = graph.nodes[hash(str([i+a,j+b]))].properties["distance"]
                            total_dist = dist2 + dist + abs(a) + abs(b)
                            if total_dist < vanilla_dist:
                                shortcuts[str([i,j])+str([i+a,j+b])] = vanilla_dist - total_dist
                    except:
                        pass
score = 0
for key, val in shortcuts.items():
    if val >= 100:
        score += 1
print("Q2 answer:", score)