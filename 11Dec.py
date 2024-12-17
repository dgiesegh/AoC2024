# -*- coding: utf-8 -*-

import _utils as u

def evolve_stone(stone):
    if stone == "0":
        return ["1"]
    elif len(stone) % 2 == 0:
        return [str(int(stone[:int(len(stone)/2)])), str(int(stone[int(len(stone)/2):]))]
    else:
        return [str(int(stone)*2024)]

def build_graph(stones, depth):
    graph = u.Graph()
    queue = stones
    for stone in queue:
        graph.add_node(stone, [0,0], [])
    new_queue = []
    for d in range(depth):
        for stone in queue:
            neighbours = evolve_stone(stone)
            for n in neighbours:
                if not graph.exists_node(n):
                    graph.add_node(n, [0,0], [])
                    graph.add_connection(stone, n, False)
                    new_queue.append(n)
                elif not graph.exists_connection(stone, n):
                    graph.add_connection(stone, n, False)
        queue = new_queue.copy()
        new_queue = []
    return graph

def traverse_graph(graph, stones, depth):
    queue = stones
    for stone in queue:
        graph.nodes[stone].properties = [1,0]
    new_queue = []
    for d in range(depth):
        for stone in queue:
            neighbours = graph.get_neighbours(stone)
            for n in neighbours:
                graph.nodes[n].properties[1] += graph.nodes[stone].properties[0]
                if n+n==stone:
                    graph.nodes[n].properties[1] += graph.nodes[stone].properties[0]
                if n not in new_queue:
                    new_queue.append(n)
        queue = new_queue.copy()
        new_queue = []
        for stone in queue:
            graph.nodes[stone].properties[0] = graph.nodes[stone].properties[1]
            graph.nodes[stone].properties[1] = 0
    score = 0
    for stone in queue:
        score += graph.nodes[stone].properties[0]
    return score

stones = u.read_lines("11Dec.txt")[0].split(" ")

stone_graph = build_graph(stones, 75)

print("Q1 answer:", traverse_graph(stone_graph, stones, 25))
print("Q2 answer:", traverse_graph(stone_graph, stones, 75))