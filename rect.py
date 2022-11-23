# Let L = length of side. Let (center_x,center_y) be the center point.

# Then edges are

# center_x - 0.5*side*(sin(theta) + cos(theta)), center_y - 0.5*side*(sin(theta) - cos(theta)),
# center_x + 0.5*side*(sin(theta) - cos(theta)), center_y - 0.5*side*(sin(theta) + cos(theta)),
# center_x + 0.5*side*(sin(theta) + cos(theta)), center_y + 0.5*side*(sin(theta) - cos(theta)),
# center_x - 0.5*side*(sin(theta) - cos(theta)), center_y + 0.5*side*(sin(theta) + cos(theta))


from math import sin
from math import cos
from math import degrees


theta=degrees(0)
center_x=10
center_y=20
length=20
height=15

print("A: ", center_x - 0.5*length*(sin(theta) + cos(theta)), center_y - 0.5*height*(sin(theta) - cos(theta)))
print("B: ", center_x + 0.5*length*(sin(theta) - cos(theta)), center_y - 0.5*height*(sin(theta) + cos(theta)))
print("C: ", center_x + 0.5*length*(sin(theta) + cos(theta)), center_y + 0.5*height*(sin(theta) - cos(theta)))
print("D: ", center_x - 0.5*length*(sin(theta) - cos(theta)), center_y + 0.5*height*(sin(theta) + cos(theta)))