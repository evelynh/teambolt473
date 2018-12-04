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

p = [[4.34, 60.0], [33.79, 27.3], [60.0, 58.77], [10.21, 5.38], [-35.81, 24.92], [-60.0, -9.39], [-28.08, 50.65], [14.25, 60.0], [-18.18, -16.4], [-60.0, -32.48], [-23.06, 14.8], [-36.8, 59.74], [12.45, 60.0], [31.16, -1.2]]
print(generate_wolf(p, [34.8, 0], 90))

