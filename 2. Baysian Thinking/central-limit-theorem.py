from helpers import *
import numpy as np
import matplotlib.pyplot as plt

def random_sample(population_data, sample_size):
    """
    create a list of sample_size from population_data randomly
    """
    return np.random.choice(population_data, size = sample_size)

def sample_mean(sample):
    """
    find the mean of the sample list
    """
    return np.mean(sample)

def central_limit_theorem(population, sample_size, iterations):
    """
    generate the list of means of all lists each of sample size, for n iterations
    """
    sample_means_results = []
    for i in range(iterations):
        # get a random sample from the population of size n
        sample = random_sample(population, sample_size)
        sample_means_results.append(sample_mean(sample))
    return sample_means_results

def visualize_results(sample_means):

    plt.hist(sample_means, bins = 30)
    plt.title('Histogram of the Sample Means')
    plt.xlabel('Mean Value')
    plt.ylabel('Count')
    plt.show(block=True)

population_data = distribution(50, 10000, 100)
#histogram_visualization(population_data)
sample_means_results = central_limit_theorem(population_data, 1000, 10000)
visualize_results(sample_means_results)