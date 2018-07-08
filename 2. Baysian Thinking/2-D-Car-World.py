def initial_grid(rows, columns):

    # TODO: initialize an empty list in a variable called grid
    grid = []

    # TODO: initialize an empty row in a variable called row
    row = []

    if (rows > 0 and columns > 0):
        probability = 1/((rows)*(columns))
        for index_row in range(rows):
            row = []
            for index_column in range(columns):
                row.append(probability)
            grid.append(row)
    return grid

def probability(grid, row, column):
    """
    outputs the probability that the robot is at a specific point on the grid
    """
    if(row < len(grid) and column < len(grid[0])):
        return grid[row][column]
    else:
        return None

def update_probability(grid, update_list):
    """
    update probabilities on the grid
    """
    for each_row in update_list:
        #print("Row: " + str(each_row[0][0]) + " Column: " + str(each_row[0][1]) + " Prob: " + str(each_row[1]))
        grid[each_row[0][0]][each_row[0][1]] = each_row[1]
    
    return grid

grid = [[.05, .1, .1],
        [.04, .3, .02],
        [.01, .023, .017],
        [.005, .012, .06],
        [.09, .07, .103]]

update_list = [
              [[4,2], 0.012],
              [[2,2], 0.108],
              [[0,1], 0.004],
              [[3,0], 0.101]
              ]
print(update_probability(grid, update_list))