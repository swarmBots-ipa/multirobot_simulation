# Let L = width of side. Let (center_x,center_y) be the center point.

# Then edges are


# print("A: ", center_x - 0.5*width*(sin(angle) + cos(angle)), center_y - 0.5*height*(sin(angle) - cos(angle)))
# print("B: ", center_x + 0.5*width*(sin(angle) - cos(angle)), center_y - 0.5*height*(sin(angle) + cos(angle)))
# print("C: ", center_x + 0.5*width*(sin(angle) + cos(angle)), center_y + 0.5*height*(sin(angle) - cos(angle)))
# print("D: ", center_x - 0.5*width*(sin(angle) - cos(angle)), center_y + 0.5*height*(sin(angle) + cos(angle)))


from math import sin
from math import cos
from math import degrees, radians
from math import sqrt

from matplotlib import pyplot as plt
from shapely.geometry import Polygon


angle = radians(180)
center_x = 50
center_y = 50
width = 20
height = 40
p = sqrt(width*width+height*height)/2
# top right
print("A: ", (center_x + ((width *0.5) * cos(angle)) - ((height *0.5) * sin(angle)),
              center_y + ((width *0.5) * sin(angle)) + ((height *0.5) * cos(angle))))
#top left
print("B: ", (center_x - ((width *0.5) * cos(angle)) - ((height *0.5) * sin(angle)),
              center_y - ((width *0.5) * sin(angle)) + ((height *0.5) * cos(angle))))
#bottom left
print("C: ", (center_x - ((width *0.5) * cos(angle)) + ((height *0.5) * sin(angle)),
              center_y - ((width *0.5) * sin(angle)) - ((height *0.5) * cos(angle))))
#bottom right
print("D: ", (center_x + ((width *0.5) * cos(angle)) + ((height *0.5) * sin(angle)),
              center_y + ((width *0.5) * sin(angle)) - ((height *0.5) * cos(angle))))


fig, ax=plt.subplots()
poly=Polygon([(center_x + ((width *0.5) * cos(angle)) - ((height *0.5) * sin(angle)),
                center_y + ((width *0.5) * sin(angle)) + ((height *0.5) * cos(angle))),
                (center_x - ((width *0.5) * cos(angle)) - ((height *0.5) * sin(angle)),
                 center_y - ((width *0.5) * sin(angle)) + ((height *0.5) * cos(angle))),
                (center_x - ((width *0.5) * cos(angle)) + ((height *0.5) * sin(angle)),
                 center_y - ((width *0.5) * sin(angle)) - ((height *0.5) * cos(angle))),
                (center_x + ((width *0.5) * cos(angle)) + ((height *0.5) * sin(angle)),
                center_y + ((width *0.5) * sin(angle)) - ((height *0.5) * cos(angle)))])
x, y=poly.exterior.xy
ax.plot(x, y)
plt.axis([0, 100, 1, 100])
plt.show()
