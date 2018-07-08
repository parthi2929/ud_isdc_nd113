import matplotlib as mpl
import matplotlib.pyplot as plt

import numpy as np

def initialize_robot(grid_size):
    """
    returns a list containing the initial probability for each space on the grid
    """
    initial_probability = 1/grid_size    
    return [initial_probability]*grid_size

def grid_probability(grid, position):
    """
    outputs the probability that the robot is at a specific point on the grid
    """
    if(position < len(grid)):
        return grid[position]
    else:
        return None

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
    plt.xlabel('Grid Space')
    plt.ylabel('Probability')

    # Show graphic

    # if running in IPython
    plt.show()

    # if running in python shell
    plt.show(block=True)
    
def update_probabilities(grid, updates):
        
    for each_row in updates:
        grid[each_row[0]] = each_row[1]

    return grid

output_map([.2, .2, .2, .2, .2])