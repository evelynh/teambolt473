import random
import math
import sys

def wolf_go_to(prev_point, point, sheepPoint, angle):
    #Based on point, generate a random point within an angle tolerance
    new_point = []
    d_x = point[0] + sheepPoint[0] - prev_point[0]
    d_y = point[1] + sheepPoint[1] - prev_point[1]
    theta = math.atan2(d_y , d_x);
    distance = math.sqrt(d_x**2 + d_y**2)
    r = random.randrange(0, angle*2 + 1)
    #print('random ', r, ' angle ', angle)
    newTheta = (theta*180/math.pi) + r - angle
    newTheta = newTheta*math.pi/180
    new_x = round(prev_point[0] + (distance * math.cos(newTheta)), 2)
    new_y = round(prev_point[1] + (distance * math.sin(newTheta)), 2)
    while abs(new_x - sheepPoint[0]) > 60 or abs(new_y - sheepPoint[1]) > 60:
        r = random.randrange(0, angle*2 + 1)
        newTheta = (theta*180/math.pi) + r - angle
        newTheta = newTheta*math.pi/180
        new_x = round(prev_point[0] + (distance * math.cos(newTheta)), 2)
        new_y = round(prev_point[1] + (distance * math.sin(newTheta)), 2)
    #new_point.append(round(prev_point[0] + (distance * math.cos(newTheta)), 2))
    #new_point.append(round(prev_point[1] + (distance * math.sin(newTheta)), 2))
    new_point = [new_x, new_y]
    sys.stderr.write(str(new_point)+"\n")
    return new_point

def generate_wolf(p, sheepPoint, angle):
    sys.stderr.write("given points: \n")
    final = []
    sys.stderr.write(str(p)  + "\n")
    points = p[:]
    prev_point = points[0]
    points.pop()
    #sys.stderr.write("popped points: \n") 
    #sys.stderr.write(str(points)  + "\n")
    for i in range(0, len(points)):
        prev_point = wolf_go_to(prev_point, points[i], sheepPoint, angle)
        final.append(prev_point)
    return final

p = [[0.0, 0.0], [60.0, -20.66], [41.09, -27.17], [22.68, -19.36], [12.38, -2.21], [2.99, 15.45], [-8.19, 32.03], [-23.95, 44.34], [-43.88, 46.08], [-60.0, 37.51], [-42.34, 28.12], [-29.22, 13.03], [-9.37, 10.59], [8.12, 20.29], [20.16, 36.26], [35.92, 48.57], [55.77, 46.13], [60.0, 42.19], [45.37, 28.55], [41.56, 8.92], [27.66, -5.47], [9.54, -13.92], [-10.16, -17.39], [-27.12, -6.8], [-46.75, -2.98], [-60.0, 6.3], [-43.62, 17.77], [-31.58, 33.74], [-19.54, 49.71], [-8.89, 60.0], [5.49, 46.11], [25.48, 45.41], [39.12, 30.78], [53.51, 16.89], [60.0, 15.27], [40.59, 10.43], [23.63, -0.17], [12.45, -16.75], [-5.04, -26.44]]
print(generate_wolf(p, [0, 30.48], 90))

