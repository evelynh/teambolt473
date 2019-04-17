import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

import paths

def intermediates(p1, p2, nb_points=100):
    """"Return a list of nb_points equally spaced points
    between p1 and p2"""
    # If we have 8 intermediate points, we have 8+1=9 spaces
    # between p1 and p2
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

orig_gen_paths = paths.generate_set([0,0], 750, 60, 60, num_circs)
# code to convert points into usable format

min_length = float("inf")
for i in range(0, num_circs):
    curr_length = len(orig_gen_paths[i])
    if curr_length < min_length:
        min_length = curr_length

gen_paths = []

for i in range(0, num_circs):
    gen_paths.append(orig_gen_paths[i][:min_length])

x_comp = []
y_comp = []

for i in range(0, num_circs):
    x_data, y_data = reformat(gen_paths[i])
    x_comp.append(x_data)
    y_comp.append(y_data)

# code to animate
fig = plt.figure()
ax = fig.add_subplot(111)

plt.xlim(-100, 100)
plt.ylim(-100, 100)
plt.axis('off')
fig.patch.set_facecolor((0, 0, 0))

circs = []

for a in range(num_circs):
    curr_circle = plt.Circle((5, -5), 5, ec='w', fc='k')
    print(x_comp[a][0])
    curr_circle.center = (x_comp[a][0], y_comp[a][0])  
    circs.append(curr_circle)

def init():
    for a in range(num_circs):
        ax.add_patch(circs[a])
    return circs

def animate(i):
    for a in range(num_circs):
        x = x_comp[a][i]
        y = y_comp[a][i]
        circs[a].center = (x, y) 
    return circs

anim = animation.FuncAnimation(fig, animate, 
                               init_func=init, 
                               frames=min_length*100, 
                               interval=10,
                               blit=True)

plt.show()