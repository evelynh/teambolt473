import math
import random


def generate_point(point, angle, dist, x_max, y_max):
    '''
    Calculate point at distance and angle away from inputted point
    If that calculated point is within bounds, return calculated points
    Otherwise, adjust x and y as needed so point is within bounds
    '''
    #print("new point being generated with angle %f" % angle)
    x = point[0] + dist*math.cos(angle*math.pi/180)
    y = point[1] + dist*math.sin(angle*math.pi/180)
    #print("originals x:" + str(x) + " y:" + str(y))
    if abs(x) > x_max:
    	if x > 0: x_new = x_max 
    	else: x_new = - x_max
    	y = (y - point[1])/(x - point[0]) * (x_new - point[0]) + point[1]
    	x = x_new
    if abs(y) > y_max:
    	if y > 0: y_new = y_max 
    	else: y_new = - y_max
    	x = (x - point[0])/(y - point[1]) * (y_new - point[1]) + point[0]
    	y = y_new
    return [x, y]

def calc_dist(A, B):
    '''
    Calculate distance between A and B
    '''
    dist = math.sqrt((B[0]-A[0])**2 + (B[1]-A[1])**2)
    return dist


def calc_total_dist(points):
    '''
    Calculate total distance travelled by set of points
    '''
    total_dist = 0
    if len(points) <= 2:
        return 0
    for i in range(0, len(points)-1):
        a = points[i]
        b = points[i+1]
        total_dist += calc_dist(a, b)
    return round(total_dist,2)
        
def round_points(points):
    '''
    Round points to have maximum 2 decimal points
    '''
    rounded = points
    for i in range(0, len(points)):
        rounded[i] = [round(points[i][0], 2), round(points[i][1], 2)]
    return rounded

def remove_repeats(points):
    '''
    Remove consecutive points that are repeats, which causes issues for Sphero robots
    ex. [[0,0], [50,50], [50,50]] -> [[0,0], [50,50]]
    '''
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
    '''
    If after removing all the bad points, distance is less than 100, know to discard that set of points.
    Returns true if path distance for the last 4 points adds up to less than a 100
    '''
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
    '''
    Generate path given specified inputs:
        start = starting point
        tot_distance = total distance of path
        x_max: maximum distance in +x and -x direction
        y_max: maximum distance in +y and -y direction
    '''
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
      	#print("dist remaining %f" % dist_remain)
      	#print(points)
      	prev_point = points[len(points)-1]

      	#rebound condition corners
      	if abs(prev_point[0]) == x_max and abs(prev_point[1]) == y_max:
      		r_angle = (r_angle + 180) % 360
      	#rebound condition right or left edge
      	elif abs(prev_point[0]) == x_max:
      		r_angle = (180 - r_angle) % 360
      	#rebound condition bottom or top edge
      	elif abs(prev_point[1]) == y_max:
      		r_angle = 360 - r_angle
        #non rebound
      	else:
            angle1 = random.randrange(0, 45, 3)
            angle2 = random.randrange(-45, 0, 3)
            chooseangle = random.randint(1,2)
            if chooseangle == 1:
                r_angle = (r_angle + angle1) % 360
            else:
                r_angle = (r_angle + angle2) % 360
      	r_dist = 30
      	gen_point = generate_point(curr_point, r_angle, r_dist, x_max, y_max)
      	dist = calc_dist(curr_point, gen_point)
      	dist_remain = dist_remain - dist
      	points += [gen_point]
      	curr_point = gen_point
    points = round_points(points)
    test = remove_repeats(points)
    if (round(calc_total_dist(points), 2) != round(calc_total_dist(test), 2)):
        return -1
    # if(is_bad_path(test)):
    # 	print("IS BAD PATH")
    #   	return -1
    if (round(calc_total_dist(test), 2) < 200):
        return -1
    return test

def generate_set(start, tot_dist, x_max, y_max, n):
    '''
    Generate set of n paths with all with the same parameters
        start = starting point
        tot_distance = total distance of path
        x_max: maximum distance in +x and -x direction
        y_max: maximum distance in +y and -y direction    
    '''
    printed = 0
    toReturn = []
    while printed < n:
    	points = generate_path(start, tot_dist, x_max, y_max)
    	if points != -1:
        	toReturn += [points]
        	printed += 1
    	else:
        	print("REJECTED")
    return toReturn

#print(generate_set([0,0], 750, 60, 60, 1))
