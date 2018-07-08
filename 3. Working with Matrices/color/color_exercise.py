# Notice we are importing the color class!

import numpy as np
import color

color1 = color.Color(250, 0, 0)
print(color1)
color2 = color.Color(0, 50, 200)
print(color2)
# Add the two colors to create a *new* color object
new_color = color1 + color2
print(new_color)