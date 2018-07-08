#Given the list motions=[1,1] which means the robot 
#moves right and then right again, compute the posterior 
#distribution if the robot first senses red, then moves 
#right one, then senses green, then moves right again, 
#starting with a uniform prior distribution.

p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
pHit = 0.6
pMiss = 0.2

def sense(p, Z):
    """
    p = initial probability distribution list
    Z = each measurement
    q = new normalized distribution list
    """
    q = []
    for each_index in range(len(p)):
        if (world[each_index] == Z):    #joint probability
            q.append(p[each_index]*pHit)
        else:
            q.append(p[each_index]*pMiss)
    total = sum(q)
    q = [ x/total for x in q]   #normalization
    return q

pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1
def move(p, U):
    """
    p = given probability distribution list
    U = amount of steps robot has moved to right (assumed as right for now)
    """
    # INEXACT MOTION
    q = [ 0 for _ in p ]
    temp = [pUndershoot, pExact, pOvershoot]
    for i in range(len(p)):

        undershoot_index    = (i + (U-1)) % len(p)
        exact_index         = (i + (U)) % len(p)
        overshoot_index     = (i + (U+1)) % len(p)

        #print(i , undershoot_index , exact_index, overshoot_index, q)

        q[ undershoot_index ]   = p[i]*temp[0] + q[ undershoot_index ]
        q[ exact_index ]        = p[i]*temp[1] + q[ exact_index ]
        q[ overshoot_index ]    = p[i]*temp[2] + q[ overshoot_index ]
    return q

import matplotlib.pyplot as plt
def output_map(grid):
    """
    outputs a bar chart showing the probabilities of each grid space
    """
    x_labels = []
    for index in range(len(grid)):
        x_labels.append(index)
    plt.bar(x_labels, grid)
 
    # Create names on the axes
    plt.title('Probability of the robot being at each space on the grid')
    plt.xlabel('1D Space')
    plt.ylabel('Probability')

    # Show graphic
    plt.show(block=True)
#
# ADD CODE HERE
#
# for each_index in range(len(measurements)):
#     p = sense(p, measurements[each_index])
measurements = ['red', 'red']
motions = [1,1]

for i in range(len(measurements)):
    p = sense(p, measurements[i])
    p = move(p, motions[i])
        
print(p) 
output_map(p)      
