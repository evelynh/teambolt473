#!python3

import paths
import generate_wolf
import generate_csv

import sys
import random
import csv

# Generate paths for each sphero
total_trials = 30

# special contains all trials that have chasing
# We used an online random generate to decide which trials those would be 

special = {}
trans = 30.48


relative_coord = [[-1 for x in range(5)] for x in range(5)]

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

#Alternatively, if want chase present and chase absent trials to be mixed, specify which trials have wolf sheep pairs by adding key to dictionary

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

def generate_paths(total_trials):
    '''Generates paths for each sphero'''
    sphero0 = paths.generate_set([0,0], 750, 60, 60, total_trials)
    sphero1 = paths.generate_set([0,0], 750, 60, 60, total_trials)
    sphero2 = paths.generate_set([0,0], 750, 60, 60, total_trials)
    sphero3 = paths.generate_set([0,0], 750, 60, 60, total_trials)
    sphero4 = paths.generate_set([0,0], 750, 60, 60, total_trials)

    compiled_paths = [sphero0, sphero1, sphero2, sphero3, sphero4]
    return compiled_paths

def chase_trials(unique_wolf_sheep, repeat_trial):
    '''This can be used to generate trials all of which contain chasing
        unique_wolf_sheep: number of unique wolf and sheep pairs
        repeat_trial: the number of times path is generated with the same wolf sheep pair'''
    ws_pairs = []
    for i in range(unique_wolf_sheep):
        angle = i//4 * 30
        sys.stderr.write(str(angle))
        wolf = random.randint(0, 4)
        sheep = random.randint(0, 4)
        while wolf == sheep:
            sheep = random.randint(0, 4)
        sys.stderr.write(str(wolf) + " " + str(sheep) + "\n")
        #random.randint(-2, 3)
        for j in range(repeat_trial):
            print(str(i*3 + j) + " " +  str(wolf) + " " + str(sheep) + " " + str(relative_coord[wolf][sheep]) + " " + str(angle)+ "\n")
            ws_pairs+=[[wolf, sheep]]
            special[i*3 + j]= [[wolf, sheep], relative_coord[wolf][sheep], angle]

    #Output wolf,sheep pairs to CSV for Matlab
    sys.stderr.write(str(ws_pairs))
    generate_csv.convert_to_ws_csv(ws_pairs)
    return special

def replace_chase_trials(compiled_paths, special):
    '''Replace trials with chasing as needed'''
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

    return compiled_paths

#Print out paths
def generate_trials():
    initial_paths = generate_paths(total_trials)
    repeats = 3
    unique = total_trials//repeats
    wolf_sheep_data = chase_trials(unique, repeats)
    final_paths = replace_chase_trials(initial_paths, wolf_sheep_data)
    print("------------------------------------------------------------------------")          
    for i in range(0, len(final_paths)):
        print("SPHERO " + str(i))
        print("points = [")
        for j in range(0, len(final_paths[i])):
            print(str(final_paths[i][j])+",")
            print("\n")
        print("];")
        print("------------------------------------------------------------------------")          
        #Output points to CSV for Matlab
        generate_csv.convert_to_csv(final_paths[i], i)
        
    print("FOR EASE-OF-USE")
    print("------------------------------------------------------------------------")

    #iterates through each sphero
    for i in range(0, len(final_paths)):
        print("SPHERO " + str(i))
        #iterates through j paths for ith sphero
        for j in range(0, len(final_paths[i])):
            print(str(j)+": " + str(final_paths[i][j]))
            print("\n")
            print("------------------------------------------------------------------------") 
    return final_paths

# generate_trials()