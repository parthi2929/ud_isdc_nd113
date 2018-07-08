import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def gaussian_density(x, mu, sigma):
    # TODO: Return the probability density function for the
    # Gaussian distribution. 
    factor1 = 1/(np.sqrt(2*np.pi*(np.square(sigma))))
    factor2_list = -(np.square(x-mu)/(2*np.square(sigma)))
    return  factor1*np.exp(factor2_list)

def plot_gaussian(x, mu, sigma):
    #y = gaussian_density(x,mu,sigma)
    y_pdf = norm(loc = mu, scale = sigma).pdf(x)

    plt.subplot(2, 1, 1)
    plt.plot(x,y_pdf)
    plt.title('Gaussian Probability Density Function')
    #plt.xlabel('x variable')
    plt.ylabel('probability density function')
    plt.subplots_adjust(hspace = 0.5)
    # plt.show(block=True)

    plt.subplot(2, 1, 2)
    y_cdf = norm(loc = mu, scale = sigma).cdf(x)
    plt.plot(x,y_cdf)
    plt.title('Gaussian Cumulative Density Function')
    plt.xlabel('x variable')
    plt.ylabel('cumulative density function')

    plt.show(block=True)

    return None

def plot_fill(x, x_fill_min, x_fill_max, y_fill_max, mu, sigma):
    """
    x               : x axis values (for eg, np.linspace(0,100,1000))
    x_fill_min      : min x value for area
    x_fill_max      : max x value for area
    y_max           : max y value for pdf
    """
    y_pdf = norm(loc = mu, scale = sigma).pdf(x)

    #area calculation
    x_fill = np.linspace(x_fill_min, x_fill_max, 1000)
    y_fill = norm(loc = mu, scale = sigma).pdf(x_fill)
    
    plt.plot(x, y_pdf)
    plt.fill_between(x_fill, y_fill)
    plt.ylim(0, y_fill_max)
    plt.title('Gaussian Probability Density Function')
    plt.xlabel('x variable')
    plt.ylabel('probability density function')
    plt.show(block=True)

def gaussian_probability(mean, stdev, x_low, x_high):
    # TODO: return the Gaussian distribution probability
    # that the x-value is between x_low and x_high
    
    # Use the SciPy library norm.cdf method
    y_low = norm(loc = mean, scale = stdev).cdf(x_low)    # area under -inf to x_low
    y_high = norm(loc = mean, scale = stdev).cdf(x_high)  # area under -inf to x_high
    return abs(y_high-y_low)

x = np.linspace(0, 100, 1000)
# plot_gaussian(x, 50, 10)
# print(norm(loc = 50, scale = 10).pdf(x))
# print(norm(loc = 50, scale = 10).cdf(x))


x_fill_min = 25
x_fill_max = 75
y_fill_max = 0.05
mu = 50
sigma = 10
plot_fill(x, x_fill_min, x_fill_max, y_fill_max, mu, sigma)