import numpy as np
def bar_heights(intervals, relative_probabilities, total_probability):

    delta_intervals = [intervals[i+1]-intervals[i] for i in range(len(intervals)-1)]
    area = np.multiply(delta_intervals, relative_probabilities)
    heights = [(total_probability/sum(area))*x for x in relative_probabilities]

    return heights

print(bar_heights([0, 5, 10, 16, 21, 24], [1, 5, 3, 6, 0.5], 0.05))
