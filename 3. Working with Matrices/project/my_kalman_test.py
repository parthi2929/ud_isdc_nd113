import pandas as pd
import math
import matplotlib.pyplot as plt
import matplotlib
import datagenerator
import matrix as m 
import matplotlib.pylab as pylab

matplotlib.rcParams.update({'font.size': 16})

# data_groundtruth() has the following inputs:
# Generates Data
# Input variables are:
# initial position meters
# initial velocity km/h
# final velocity (should be a negative number) km/h
# acceleration (should be a negative number) m/s^2
# how long the vehicle should idle 
# how long the vehicle should drive in reverse at constant velocity
# time between lidar measurements in milliseconds


params = {'legend.fontsize': 'x-small',
          'figure.figsize': (15, 5),
         'axes.labelsize': 'x-small',
         'axes.titlesize':'x-small',
         'xtick.labelsize':'x-small',
         'ytick.labelsize':'x-small'}
pylab.rcParams.update(params)

time_groundtruth, distance_groundtruth, velocity_groundtruth, acceleration_groundtruth = datagenerator.generate_data(5, 100, -10, -10,
                                                                                              5000, 5000, 50)
data_groundtruth = pd.DataFrame(
    {'time': time_groundtruth,
     'distance': distance_groundtruth,
     'velocity': velocity_groundtruth,
     'acceleration': acceleration_groundtruth
    })

fig, axes = plt.subplots(nrows=3, ncols=2)

ax1 = data_groundtruth.plot(kind='line', x='time', y='distance', title='Object Distance Versus Time', ax=axes[0,0])
ax1.set(xlabel='time (milliseconds)', ylabel='distance (meters)')



ax2 = data_groundtruth.plot(kind='line', x='time', y='velocity', title='Object Velocity Versus Time', ax=axes[1,0])
ax2.set(xlabel='time (milliseconds)', ylabel='velocity (km/h)')


data_groundtruth['acceleration'] = data_groundtruth['acceleration'] * 1000 / math.pow(60 * 60, 2)
ax3 = data_groundtruth.plot(kind='line', x='time', y='acceleration', title='Object Acceleration Versus Time', ax=axes[2,0])
ax3.set(xlabel='time (milliseconds)', ylabel='acceleration (m/s^2)')


# make lidar measurements
lidar_standard_deviation = 0.15
lidar_measurements = datagenerator.generate_lidar(distance_groundtruth, lidar_standard_deviation)
lidar_time = time_groundtruth

data_lidar = pd.DataFrame(
    {'time': time_groundtruth,
     'distance': distance_groundtruth,
     'lidar': lidar_measurements
    })

matplotlib.rcParams.update({'font.size': 22})

ax4 = data_lidar.plot(kind='line', x='time', y ='distance', label='ground truth', figsize=(20, 15), alpha=0.8,
               title = 'Lidar Measurements Versus Ground Truth', color='red',ax=axes[0,1])

ax5 = data_lidar.plot(kind='scatter', x ='time', y ='lidar', label='lidar measurements', ax=ax4, alpha=0.6, color='g')
ax5.set(xlabel='time (milliseconds)', ylabel='distance (meters)')


initial_distance = 0
initial_velocity = 0

x_initial = m.Matrix([[initial_distance], [initial_velocity * 1e-3 / (60 * 60)]])
P_initial = m.Matrix([[5, 0],[0, 5]])

acceleration_variance = 50
lidar_variance = math.pow(lidar_standard_deviation, 2)

H = m.Matrix([[1, 0]])
R = m.Matrix([[lidar_variance]])
I = m.identity(2)

def F_matrix(delta_t):
    return m.Matrix([[1, delta_t], [0, 1]])

def Q_matrix(delta_t, variance):
    t4 = math.pow(delta_t, 4)
    t3 = math.pow(delta_t, 3)
    t2 = math.pow(delta_t, 2)
    
    return variance * m.Matrix([[(1/4)*t4, (1/2)*t3], [(1/2)*t3, t2]])

# Kalman Filter Implementation

x = x_initial
P = P_initial

x_result = []
time_result = []
v_result = []


for i in range(len(lidar_measurements) - 1):
        
    # calculate time that has passed between lidar measurements
    delta_t = (lidar_time[i + 1] - lidar_time[i]) / 1000.0

    # Prediction Step - estimates how far the object traveled during the time interval
    F = F_matrix(delta_t)
    Q = Q_matrix(delta_t, acceleration_variance)
    
    x_prime = F * x
    P_prime = F * P * F.T() + Q
    
    # Measurement Update Step - updates belief based on lidar measurement
    y = m.Matrix([[lidar_measurements[i + 1]]]) - H * x_prime
    S = H * P_prime * H.T() + R
    K = P_prime * H.T() * S.inverse()
    x = x_prime + K * y
    P = (I - K * H) * P_prime

    # Store distance and velocity belief and current time
    x_result.append(x[0][0])
    v_result.append(3600.0/1000 * x[1][0])
    time_result.append(lidar_time[i+1])
    
result = pd.DataFrame(
    {'time': time_result,
     'distance': x_result,
     'velocity': v_result
    })

ax6 = data_lidar.plot(kind='line', x='time', y ='distance', label='ground truth', figsize=(22, 18), alpha=.3, title='Lidar versus Kalman Filter versus Ground Truth')
ax7 = data_lidar.plot(kind='scatter', x ='time', y ='lidar', label='lidar sensor', ax=ax6)
ax8 = result.plot(kind='scatter', x = 'time', y = 'distance', label='kalman', ax=ax7, color='r')
ax8.set(xlabel='time (milliseconds)', ylabel='distance (meters)')
plt.show()

fig.set_size_inches(12,10)
plt.tight_layout()  #else sub plot legends overlapping
plt.show()
