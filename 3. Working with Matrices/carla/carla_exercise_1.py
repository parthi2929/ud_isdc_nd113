import numpy as np
import car

# Create a 2D world of 0's
height = 4
width = 6
world = np.zeros((height, width))

# Define the initial car state
initial_position = [0, 0] # [y, x] (top-left corner)
velocity = [0, 1] # [vy, vx] (moving to the right)

# Create a car object with these initial params
carla = car.Car(initial_position, velocity, world)

print('Carla\'s initial state is: ' + str(carla.state))
#carla.display_world()

#--- MOVE LEFT ---
# carla.move()
# carla.move()
# carla.move()
# carla.turn_left()
# carla.move()
# carla.turn_left()
# carla.move()
# carla.move()
# carla.move()
# carla.turn_left()
# carla.move()
# carla.display_world()

#--- MOVE RIGHT ---
carla.move()
carla.move()
carla.move()
carla.turn_right()
carla.move()
carla.move()
carla.move()
carla.turn_right()
carla.move()
carla.move()
carla.move()
carla.turn_right()
carla.move()
carla.move()
carla.move()
carla.display_world()