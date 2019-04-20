import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

import paths

def intermediates(p1, p2):
    """"Return a list of nb_points equally spaced points
    between p1 and p2"""
    # If we have 8 intermediate points, we have 8+1=9 spaces
    # between p1 and p2
    dist = paths.calc_dist(p1, p2)
    nb_points = int(dist)
    x_spacing = (p2[0] - p1[0]) / (nb_points + 1)
    y_spacing = (p2[1] - p1[1]) / (nb_points + 1)

    return [[p1[0] + i * x_spacing, p1[1] +  i * y_spacing] 
            for i in range(1, nb_points+1)]

def reformat(points):
    f_points = []
    for i in range(0, len(points)-1):
        p_1 = points[i]
        p_2 = points[i+1]
        btwn = intermediates(p_1, p_2)
        for p in btwn:
            f_points.append(p)

    x_data = []
    y_data = []

    for point in f_points:
        # print(point)
        x_data.append(point[0])
        y_data.append(point[1]) 
    return x_data, y_data

num_circs = 5

origins = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
orig_gen_paths = []

for i in range(num_circs):
    orig_gen_paths.append(paths.generate_set(origins[i], 675, 80, 80, num_circs)[0])
    
orig_x_comp = []
orig_y_comp = []

for i in range(0, num_circs):
    x_data, y_data = reformat(orig_gen_paths[i])
    orig_x_comp.append(x_data)
    orig_y_comp.append(y_data)

x_comp = []
y_comp = []

min_x_length = float("inf")
for i in range(0, num_circs):
    curr_x_length = len(orig_x_comp[i])
    if curr_x_length < min_x_length:
        min_x_length = curr_x_length
min_y_length = float("inf")
for i in range(0, num_circs):
    curr_y_length = len(orig_y_comp[i])
    if curr_y_length < min_y_length:
        min_y_length = curr_y_length

for i in range(0, num_circs):
    x_comp.append(orig_x_comp[i][:min_x_length])

for i in range(0, num_circs):
    y_comp.append(orig_y_comp[i][:min_y_length])

# code to animate
fig = plt.figure()
ax = fig.add_subplot(111)

plt.xlim(-100, 100)
plt.ylim(-100, 100)
plt.axis('off')
fig.patch.set_facecolor((0, 0, 0))

circs = []
colors = ['b', 'g', 'r', 'c', 'm']
for a in range(num_circs):
    curr_circle = plt.Circle((5, -5), 5, ec='w', fc='k')
    curr_circle.center = (x_comp[a][0], y_comp[a][0])  
    circs.append(curr_circle)

def init():
    for a in range(num_circs):
        ax.add_patch(circs[a])
    return circs

def animate(i):
    for a in range(num_circs):
        if i > len(x_comp[a])-1:
            circs[a].set_facecolor(colors[a])
        else:
            x = x_comp[a][i]
            y = y_comp[a][i]
            circs[a].center = (x, y) 
    return circs

anim = animation.FuncAnimation(fig, animate, 
                               init_func=init, 
                               frames=1000, 
                               interval=30,
                               blit=True)
plt.show()
