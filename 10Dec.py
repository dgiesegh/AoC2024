# -*- coding: utf-8 -*-

import _utils as u

top = u.make_matrix_from_readlines(u.read_lines("10Dec.txt"))

topgraph = u.Graph()
trailheads = []

for i in range(top.shape[0]):
    for j in range(top.shape[1]):
        topgraph.add_node(str(i)+" "+str(j), int(top[i,j]), [])
        if top[i,j] == '0':
            trailheads.append(str(i)+" "+str(j))

for i in range(top.shape[0]):
    for j in range(top.shape[1]):
        if i-1 >= 0:
            if int(top[i,j]) - int(top[i-1,j]) == -1:
                topgraph.add_connection(str(i)+" "+str(j), str(i-1)+" "+str(j), False)
        if j-1 >= 0:
            if int(top[i,j]) - int(top[i,j-1]) == -1:
                topgraph.add_connection(str(i)+" "+str(j), str(i)+" "+str(j-1), False)
        if i+1 < top.shape[0]:
            if int(top[i,j]) - int(top[i+1,j]) == -1:
                topgraph.add_connection(str(i)+" "+str(j), str(i+1)+" "+str(j), False)
        if j+1 < top.shape[1]:
            if int(top[i,j]) - int(top[i,j+1]) == -1:
                topgraph.add_connection(str(i)+" "+str(j), str(i)+" "+str(j+1), False)

scores = {}
ratings = {}
for head in trailheads:
    #print()
    #print("Starting head", head)
    queue = [head]
    unique_nines = set()
    total_nines = 0
    while len(queue) != 0:
        node = queue.pop()
        #print("Node", node)
        if topgraph.nodes[node].properties == 9:
            unique_nines.add(node)
            total_nines += 1
        neighbours = topgraph.get_neighbours(node)
        for n in neighbours:
            queue.append(n)
    scores[head] = len(unique_nines)
    ratings[head] = total_nines

print("Q1 answer:", sum(scores.values()))
print("Q2 answer:", sum(ratings.values()))