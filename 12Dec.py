# -*- coding: utf-8 -*-

import _utils as u

plots = u.make_matrix_from_readlines(u.read_lines("12Dec.txt"))

same_type_adj = {}
diff_type_adj = {}
inds = []

for i in range(plots.shape[0]):
    for j in range(plots.shape[1]):
        plottype = plots[i,j]
        ind = str(i)+" "+str(j)
        inds.append(ind)
        same_type_adj[ind] = []
        diff_type_adj[ind] = []
        for d in [[0,1], [1,0], [-1,0], [0,-1]]:
            if i+d[0] >= 0 and i+d[0] < plots.shape[0] and j+d[1] >= 0 and j+d[1] < plots.shape[1]:
                if plots[i+d[0], j+d[1]] == plottype:
                    same_type_adj[ind].append(str(i+d[0])+" "+str(j+d[1]))
                else:
                    diff_type_adj[ind].append(str(i+d[0])+" "+str(j+d[1]))
            else:
                diff_type_adj[ind].append(str(i+d[0])+" "+str(j+d[1]))
                diff_type_adj[str(i+d[0])+" "+str(j+d[1])] = [ind]

def coords(index):
    return [int(a) for a in index.split(" ")]
def find_start_plot(outside_plot, area_plots):
    return list(set(diff_type_adj[outside_plot]) & set(area_plots))[0]
def get_sides(area_plots, outside_plots):
    next_dir = {"[0, -1]":[-1,0], "[-1, 0]":[0,1], "[0, 1]":[1,0], "[1, 0]":[0,-1]}
    prev_dir = {"[0, -1]":[1,0], "[-1, 0]":[0,-1], "[0, 1]":[-1,0], "[1, 0]":[0,1]}
    sides = 0
    while len(outside_plots) != 0:
        outside_plot = outside_plots[0]
        start_plot = find_start_plot(outside_plot, area_plots)
        i,j = coords(start_plot)
        o1,o2 = coords(outside_plot)
        curr_dir = [i-o1, j-o2]
        curr_dir = next_dir[str(curr_dir)]
        start_dir = curr_dir.copy()
        sides_now = sides
        while str(i)+" "+str(j) != start_plot or curr_dir != start_dir or sides == sides_now:
            curr_dir = next_dir[str(curr_dir)]
            i += curr_dir[0]
            j += curr_dir[1]
            if str(i)+" "+str(j) not in area_plots:
                o_plot = str(i)+" "+str(j)
                if o_plot in outside_plots:
                    outside_plots.remove(o_plot)
                i -= curr_dir[0]
                j -= curr_dir[1]
                curr_dir = prev_dir[str(curr_dir)]
                i += curr_dir[0]
                j += curr_dir[1]
                if str(i)+" "+str(j) not in area_plots:
                    i -= curr_dir[0]
                    j -= curr_dir[1]
                    curr_dir = prev_dir[str(curr_dir)]
                    sides += 1
            else:
                sides += 1
    return sides
            
total_score1 = 0
total_score2 = 0
while len(inds) != 0:
    ind = inds[0]
    queue = [ind]
    area_plots = []
    outside_plots = []
    area = 0
    perimeter = 0
    while len(queue) != 0:
        curr_ind = queue.pop()
        area_plots.append(curr_ind)
        area += 1
        for p in diff_type_adj[curr_ind]:
            perimeter += 1
            if p not in outside_plots:
                outside_plots.append(p)
        for p in same_type_adj[curr_ind]:
            if p in inds and p not in queue:
                queue.append(p)
        inds.remove(curr_ind)
    sides = get_sides(area_plots, outside_plots)
    #print("Area", area, "perim", perimeter, "sides", sides)
    score1 = area*perimeter
    score2 = sides*area
    #print("Scores", score1, score2)
    total_score1 += score1
    total_score2 += score2

print("Q1 answer:", total_score1)
print("Q2 answer:", total_score2)