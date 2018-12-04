#!python3

import paths
import generate_wolf
import generate_csv

import sys
import random
import csv

sphero0 = paths.generate_set([0,0], 750, 60, 60, 72)
sphero1 = paths.generate_set([0,0], 750, 60, 60, 72)
sphero2 = paths.generate_set([0,0], 750, 60, 60, 72)
sphero3 = paths.generate_set([0,0], 750, 60, 60, 72)
sphero4 = paths.generate_set([0,0], 750, 60, 60, 72)

compiled_paths = [sphero0, sphero1, sphero2, sphero3, sphero4]

special = {}
trans = 30.48

relative_coord = [[-1 for x in xrange(5)] for x in xrange(5)]

relative_coord[0][1] = [trans, 0]
relative_coord[0][2] = [trans/2, -trans/2]
relative_coord[0][3] = [0, -trans]
relative_coord[0][4] = [trans, -trans]

relative_coord[1][0] = [-trans, 0]
relative_coord[1][2] = [-trans/2, -trans/2]
relative_coord[1][3] = [-trans, -trans]
relative_coord[1][4] = [0, -trans]
                     
relative_coord[2][0] = [-trans/2, trans/2]
relative_coord[2][1] = [trans/2, trans/2]
relative_coord[2][3] = [-trans/2, -trans/2]
relative_coord[2][4] = [trans/2, -trans/2]

relative_coord[3][0] = [0, trans]
relative_coord[3][1] = [trans, trans]
relative_coord[3][2] = [trans/2, trans/2]
relative_coord[3][4] = [trans, 0]

relative_coord[4][0] = [-trans, trans]
relative_coord[4][1] = [0, trans]
relative_coord[4][2] = [-trans/2, trans/2]
relative_coord[4][3] = [-trans, 0]

ws_pairs = []
for i in range(24):
    angle = i//4 * 30
    sys.stderr.write(str(angle))
    wolf = random.randint(0, 4)
    sheep = random.randint(0, 4)
    while wolf == sheep:
        sheep = random.randint(0, 4)
    sys.stderr.write(str(wolf) + " " + str(sheep) + "\n")
    #random.randint(-2, 3)
    for j in range(3):
        print(str(i*3 + j) + " " +  str(wolf) + " " + str(sheep) + " " + str(relative_coord[wolf][sheep]) + " " + str(angle)+ "\n")
        ws_pairs+=[[wolf, sheep]]
        special[i*3 + j]= [[wolf, sheep], relative_coord[wolf][sheep], angle]

#Output wolf,sheep pairs to CSV for Matlab
sys.stderr.write(str(ws_pairs))
generate_csv.convert_to_ws_csv(ws_pairs)

'''
special[0] = [[4,0], [-trans, trans], 120]
special[6] = [[1,2], [-trans/2, -trans/2], 120]
special[7] = [[1,2],[-trans/2, -trans/2], 150]
special[9] = [[3,2], [trans/2, trans/2], 30]
special[10] = [[3,4], [trans, 0], 90]
special[11] = [[4,2], [-trans/2, trans/2], 0]
special[14] = [[1,4], [0, -trans], 60]
special[18] = [[4,3], [-trans, 0], 150]
special[21] = [[0,3], [0, -trans], 90]
special[22] = [[4,1], [0, trans], 30]
special[24] = [[3,4], [trans, 0], 60]
special[25] = [[1,4], [0, -trans], 0]
special[26] = [[2,0], [-trans/2, trans/2], 150]
special[27] = [[3,4], [trans, 0], 60]
special[29] = [[3,2], [trans/2, trans/2], 120]
special[32] = [[4,3], [-trans, 0], 0]
special[34] = [[3,1], [trans, trans], 30]
special[35] = [[2,0], [-trans/2, trans/2], 90]
'''
for key in special:
    info = special[key]
    wolf = info[0][0]
    sheep = info[0][1]
    sheep_path = compiled_paths[sheep][key]
    sheep_point = info[1]
    angle = info[2]
    '''
    if key == 11:
        sys.stderr.write("\n")
        sys.stderr.write("the trial we want ----------------------------------------\n")
    '''
    new_path = generate_wolf.generate_wolf(sheep_path, sheep_point, angle)
    '''
    if key == 11:
        sys.stderr.write(str(new_path))
        sys.stderr.write("end --------------------------------------------------------\n")
    '''
    compiled_paths[wolf][key] = new_path


for i in range(0, len(compiled_paths)):
    for j in range(0, len(compiled_paths[i])):
        if compiled_paths[i][j][0] == [0,0]:
            compiled_paths[i][j].pop(0)

print("------------------------------------------------------------------------")          
for i in range(0, len(compiled_paths)):
    print("SPHERO " + str(i))
    print("points = [")
    for j in range(0, len(compiled_paths[i])):
        print(str(compiled_paths[i][j])+",")
        print("\n")
    print("];")
    print("------------------------------------------------------------------------")          
    #Output points to CSV for Matlab
    generate_csv.convert_to_csv(compiled_paths[i], i)
    
print("FOR EASE-OF-USE")
print("------------------------------------------------------------------------")
for i in range(0, len(compiled_paths)):
    print("SPHERO " + str(i))
    for j in range(0, len(compiled_paths[i])):
        print(str(j)+": " + str(compiled_paths[i][j]))
        print("\n")
    print("------------------------------------------------------------------------") 
