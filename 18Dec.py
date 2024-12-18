# -*- coding: utf-8 -*-

import _utils as u

def build_graph(blocked_coords, dim):
    graph = u.Graph()
    for i in range(dim):
        for j in range(dim):
            if [i,j] not in blocked_coords:
                graph.add_node(hash(str([i,j])), {"pos":[i,j]}, [])
    for node_id in graph.nodes.keys():
        pos = graph.nodes[node_id].properties["pos"]
        pos_id_1 = hash(str([pos[0], pos[1]+1]))
        pos_id_2 = hash(str([pos[0]+1, pos[1]]))
        if pos_id_1 in graph.nodes.keys():
            graph.add_connection(pos_id_1, node_id)
        if pos_id_2 in graph.nodes.keys():
            graph.add_connection(pos_id_2, node_id)
    return graph

lines = u.read_lines("18Dec.txt")

DIM = 71
OBSTACLES = 1024

coords = [[int(a) for a in line.split(",")] for line in lines]
blocked_coords = coords[:OBSTACLES]

graph = build_graph(blocked_coords, DIM)
dist = u.dijkstra(graph, hash(str([0,0])), hash(str([DIM-1,DIM-1])))

print("Q1 answer:", dist)

# answer: i = 1854
# ugly, but works
i = 0
while True:
    i += 1
    print(i)
    blocked_coords = coords[:OBSTACLES+i]
    graph = build_graph(blocked_coords, DIM)
    u.dijkstra(graph, hash(str([0,0])), 0, 1000000)
    dist = graph.nodes[hash(str([DIM-1, DIM-1]))].properties["distance"]
    if dist == 1000000:
        break

print("Q2 answer:", coords[OBSTACLES+i-1])