#created for adding relevant code snipped in blog along with quick test.abs

#sense function:


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
        if (world[each_index] == Z):
            q.append(p[each_index]*pHit)
        else:
            q.append(p[each_index]*pMiss)
    total = sum(q)
    q = [ x/total for x in q]
    return q

# p=[0.2, 0.2, 0.2, 0.2, 0.2]
# print("Prior probability: " + str(p))
# for i in range(1000):
#     p = sense(p, 'red')
# print("Posterior probability: " + str(sense(p,'red')))

p=[0, 0.5, 0, 0.5, 0]
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
        q[ undershoot_index ]   = p[i]*temp[0] + q[ undershoot_index ]
        q[ exact_index ]        = p[i]*temp[1] + q[ exact_index ]
        q[ overshoot_index ]    = p[i]*temp[2] + q[ overshoot_index ]

    return q

# p=[0, 0.5, 0, 0.5, 0]
# print("Prior probability: " + str(p))
# for i in range(1000):
#     p = move(p,2)
# print("Posterior probability: " + str(move(p,2)))

#Just for visualization
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
    plt.show(block=True)

#initial probability
p=[0.2, 0.2, 0.2, 0.2, 0.2]

#sense
world=['green', 'red', 'red', 'green', 'green']
pHit = 0.6
pMiss = 0.2

#move
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

#our operation
print("Prior probability: " + str(p))
p = sense(p, 'red') 
p = move(p , 1)
p = sense(p , 'green')
print("Posterior probability: " + str(p))
output_map(p)

