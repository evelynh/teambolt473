import math
import random

def generate_point(point, angle, dist, x_max, y_max):
    x = point[0] + dist*math.cos(angle*math.pi/180)
    y = point[1] + dist*math.sin(angle*math.pi/180)
    if abs(x) > x_max:
        if x < 0:
            x = -x_max
        else:
            x = x_max
    if abs(y) > y_max:
        if y < 0:
            y = -y_max
        else:
            y = y_max
    return [x, y]

def calc_dist(A, B):
    dist = math.sqrt((B[0]-A[0])**2 + (B[1]-A[1])**2)
    return dist


def calc_total_dist(points):
    total_dist = 0
    if len(points) <= 2:
        return 0
    for i in range(0, len(points)-1):
        a = points[i]
        b = points[i+1]
        total_dist += calc_dist(a, b)
    return round(total_dist,2)
        
def round_points(points):
    rounded = points
    for i in range(0, len(points)):
        rounded[i] = [round(points[i][0], 2), round(points[i][1], 2)]
    return rounded
'''
def shorten_path(points):
    while calc_total_dist(points) > 501 and len(points)>3:
        points.pop(len(points)-2)
    return points
'''

def remove_repeats(points):
    toReturn = []
    i = 0
    while i < len(points)-1:
        if points[i] == points[i+1]:
            toReturn +=[points[i]]
            while i < len(points)-1 and points[i] == points[i+1]:
                i= i+1
            i = i+1
        else:
            toReturn += [points[i]]
            i=i+1
    if points[len(points)-2] != points[len(points)-1]:
        toReturn += [points[i]]   
    return toReturn

def is_bad_path(points):
    start = 1
    end = -1
    tot_cur_dist = 0
    for i in range(1, 4):
        tot_cur_dist += calc_dist(points[i-1], points[i])
        end = i
    for i in range(4, len(points)):
        if tot_cur_dist < 100:
            return True
        tot_cur_dist -= calc_dist(points[start-1], points[start])
        start+=1
        tot_cur_dist += calc_dist(points[end], points[i])
        end+=1
    return False


def generate_path(start, tot_dist, x_max, y_max):
    curr_point = start
    points = [start]
    dist_remain = tot_dist
    max_dist = int(calc_dist(start, [x_max, y_max]))
    r_angle = random.randint(0,359)
    r_dist = random.randint(30, max_dist)
    gen_point = generate_point(curr_point, r_angle, r_dist, x_max, y_max)
    dist = calc_dist(curr_point, gen_point)
    dist_remain = dist_remain - dist
    points += [gen_point]
    curr_point = gen_point

    while dist_remain > 0:
        prev_point = points[len(points)-1]
        if abs(prev_point[0]) == x_max or abs(prev_point[1]) == y_max:
            '''
            # print("hi") 
            if 0 <= r_angle < 45:
                r_angle = r_angle + 100
            elif 45 <= r_angle < 90:
                r_angle = 90 + (90 - r_angle)
            elif 90 <= r_angle < 135:
                r_angle = r_angle + 100
            elif 135 <= r_angle < 180:
                r_angle = 180+(r_angle-90)
            elif 180 <= r_angle < 225:
                r_angle = r_angle + 100
            elif 225 <= r_angle < 270:
                r_angle = 270 + (90-(180-r_angle))
            elif 270 <= r_angle < 315:
                r_angle = r_angle + 100
            else:
                r_angle = 360-r_angle
            '''
            add = random.randrange(200,270, 5)
            r_angle = (r_angle + add) % 360
            # rand = random.randrange(-1,1)
        else:
            angle1 = random.randrange(10, 80, 5)
            angle2 = random.randrange(280, 350, 5)
            chooseangle = random.randint(1,2)
            if chooseangle == 1:
                r_angle = (r_angle + angle1) % 360
            else:
                r_angle = (r_angle + angle2) % 360
            # rand = 1 
        r_dist = random.randint(40, max_dist)
        gen_point = generate_point(curr_point, r_angle, r_dist, x_max, y_max)
        dist = calc_dist(curr_point, gen_point)
        if dist <= 35:
            continue
        dist_remain = dist_remain - dist
        points += [gen_point]
        curr_point = gen_point
    points = round_points(points)
    test = remove_repeats(points)
    if (round(calc_total_dist(points), 2) != round(calc_total_dist(test), 2)):
        return -1
    if(is_bad_path(test)):
      	return -1
    if (round(calc_total_dist(test), 2) < 500):
        return -1
    return test

def generate_set(start, tot_dist, x_max, y_max, n):
    printed = 0
    toReturn = []
    while printed < n:
        points = generate_path(start, tot_dist, x_max, y_max)
        if points != -1:
            toReturn += [points]
            printed += 1
    return toReturn
          
