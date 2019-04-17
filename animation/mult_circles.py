import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

# code to convert points into usable format

points1 = [[0,0], [23.35, 19.59], [42.84, 52.13], [-6.0, 53.03], [31.97, 19.3], [13.62, 30.59], [1.95, 45.15], [-18.03, 42.95], [-30.45, 72.89], [-44.36, 72.23], [-47.68, 56.37], [-49.91, 61.71], [-37.12, 37.3], [-14.83, 20.34], [-44.02, 44.85], [23.78, 43.47], [54.89, 64.58], [52.42, 76.39], [56.79, 83.62], [32.87, 70.85], [42.11, 39.56], [23.56, 30.83], [25.83, 10.95], [-9.98, 6.81], [-33.99, 5.36], [-50.74, 24.66], [-56.79, 38.66], [-44.51, 49.36], [-45.53, 69.03], [-17.84, 63.26], [9.73, 71.06], [2.95, 69.44], [22.61, 82.2], [5.92, 61.4], [44.24, 29.89], [47.67, 51.98], [38.95, 42.15], [21.3, 50.12], [-1.07, 20.08]]
# points = [[23.35, 19.59], [42.84, 52.13]]
points2 = [[50, 50], [-4.24, 30.18], [41.17, 36.76], [54.57, 8.83], [59.66, 11.61], [39.97, 14.61], [39.67, -12.8], [8.87, -20.43], [-4.79, -3.04], [-27.87, -1.95], [-45.04, -11.51], [-56.48, 9.74], [-46.7, 22.14], [-23.42, 20.72], [-5.66, 7.08], [8.3, -3.02], [30.55, -6.18], [54.24, 2.68], [55.72, 13.14], [42.78, 3.88], [30.17, -9.65], [16.16, -20.07], [9.92, -28.18], [8.85, -10.62], [-7.35, 2.02], [10.25, 21.22], [16.83, 42.5], [5.48, 62.03], [-0.37, 81.16], [2.55, 90.26], [-5.2, 72.18], [-13.36, 56.46], [-12.76, 33.04], [-3.32, 11.87], [11.69, -4.98], [32.17, -2.36], [49.56, -21.45], [51.69, -29.42], [56.8, -10.35], [58.88, -6.58], [48.52, 9.32], [59.07, 28.25]]
points2 = points2[:len(points1)]

points3 = [[-50,-50], [10.42, 28.64], [59.78, 15.77], [40.22, 17.24], [22.91, 5.86], [-0.0, 9.72], [-16.58, 23.73], [-25.98, 39.17], [-47.6, 21.0], [-59.54, 26.84], [-40.59, 22.1], [-23.8, 38.72], [-8.44, 49.65], [12.55, 50.51], [26.81, 64.91], [45.72, 47.25], [57.84, 59.74], [39.48, 57.19], [22.18, 50.29], [4.61, 69.8], [-3.99, 87.72], [-7.79, 88.82], [3.42, 74.16], [-1.69, 50.22], [-2.86, 31.0], [6.66, 11.3], [27.96, 6.2], [45.65, -4.12], [53.17, -20.53], [44.83, -28.17], [33.93, -27.23], [14.99, -23.34], [-4.34, -28.18], [-16.44, -24.74], [-35.19, -26.3], [-48.56, -5.44], [-58.77, 6.81], [-41.63, 13.4], [-26.01, 24.36]]

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

x_data1, y_data1 = reformat(points1)
x_data2, y_data2 = reformat(points2)
x_data3, y_data3 = reformat(points3)

x_comp = [x_data1, x_data2, x_data3]
y_comp = [y_data1, y_data2, y_data3]
# code to animate

fig = plt.figure()
ax = fig.add_subplot(111)

plt.xlim(-100, 100)
plt.ylim(-100, 100)


num_circs = 3
circs = []

for a in range(num_circs):
    curr_circle = plt.Circle((5, -5), 5, fc='y')
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
                               frames=len(points1)*100, 
                               interval=10,
                               blit=True)

plt.show()