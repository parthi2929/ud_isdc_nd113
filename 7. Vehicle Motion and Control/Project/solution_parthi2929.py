import numpy as np
from math import sin, cos, pi
from matplotlib import pyplot as plt

class Vehicle:
    def __init__(self):
        self.x       = 0.0 # meters
        self.y       = 0.0
        self.heading = 0.0 # radians
        self.history = []
        
    def drive_forward(self, displacement):
        """
        Updates x and y coordinates of vehicle based on 
        heading and appends previous (x,y) position to
        history.
        """
        self.history.append((self.x, self.y))
        self.x += displacement * cos(self.heading)
        self.y += displacement * sin(self.heading)
    
    def set_heading(self, heading_in_degrees):
        """
        Sets the current heading (in radians) to a new value
        based on heading_in_degrees. Vehicle heading is always
        between 0 and 2 * pi.
        """
        heading_in_degrees = heading_in_degrees % 360 # just to be sure its always within 360
        self.heading = heading_in_degrees*pi/180
    
    def turn(self, angle_in_degrees):
        """
        Changes the vehicle's heading by angle_in_degrees. Vehicle 
        heading is always between 0 and 2 * pi.
        """
        self.heading += angle_in_degrees*pi/180
    
    def show_trajectory(self):
        """
        Creates a scatter plot of vehicle's trajectory.
        """
        X = [row[0] for row in self.history]
        Y = [row[1] for row in self.history]
        
        # DO NOT FORGET TO INCLUDE CURRENT POSITION AS WELL
        X.append(self.x)
        Y.append(self.y)        
        
        plt.scatter(X,Y)
        plt.plot(X,Y)
        plt.show()
        
    def get_trajectory(self):
        """
        returns vehicle's trajectory.
        """
        X = [row[0] for row in self.history]
        Y = [row[1] for row in self.history]
        
        # DO NOT FORGET TO INCLUDE CURRENT POSITION AS WELL
        X.append(self.x)
        Y.append(self.y)        
        
        return zip(X,Y)
    
def get_integral_from_data(data, times):

    if (len(data) != len(times)):
        raise ValueError("Arguments must be of equal length")
        
    total_area = 0    
    area_trace = [0]   # we need to generate a list of cumulative area sums till any instant
    
    prev_tim = times[0]
    for i in range(1, len(times)):
        
        curr_tim = times[i]
        
        delta_t = curr_tim - prev_tim
        delta_x = data[i]  # its just the height, as rectangle, same at both curr and prev instances
        
        area = delta_t * delta_x
        
        total_area += area
        
        prev_tim = curr_tim
        
        area_trace.append(total_area)
            
    return area_trace

def get_derivative_from_data(position_data, time_data):
    
    if (len(position_data) != len(time_data)):
        raise ValueError('Arguments length not matching')
        
    prev_pos = position_data[0]
    prev_tim = time_data[0]
    
    slopes = [0]  # assuming initial speed as zero
    
    for i in range(1,len(position_data)):
        
        curr_pos = position_data[i]
        curr_tim = time_data[i]
        
        delta_pos = curr_pos - prev_pos
        delta_tim = curr_tim - prev_tim
        
        slope = delta_pos/delta_tim
        
        slopes.append(slope)
        
        prev_pos = curr_pos
        prev_tim = curr_tim
    
    return slopes