import csv

def p_to_m(array):
    '''
    Convert point array from Python outputed array to format Matlab can use to plot
    '''
    x = [0]
    y = [0]
    for i in range(0, len(array)):
        x+=[array[i][0]]
        y+=[array[i][1]]
    return x, y

def convert_to_ws_csv(points):
    filename = 'ws_pairs.csv'
    with open(filename, 'wb') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(points)

def convert_to_csv(points, sphero):
    filename = 'Sphero'+str(sphero)+'_p2m_points.csv'
    with open(filename, 'wb') as csvfile:
        writer = csv.writer(csvfile)
        compiled = []
        for i in points:
            x, y = p_to_m(i)
            compiled += [x]
            compiled += [y]
        writer.writerows(compiled)

        
