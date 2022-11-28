import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle

#center of rectangle
X = 2698.77 
Y = 1283.01
center = np.array([[X],[Y]])

angle_deg = 83.5694 #angle rectangle
angle = math.radians(angle_deg)

# rectangle's dimension
width = 2022.23
height = 1978.78

R_lt = np.array([[np.cos(angle),-np.sin(angle)],[-np.sin(angle),-np.cos(angle)]])
A = np.dot(R_lt,np.array([[width/2], [height/2]])) + center

R_rt = np.array([[np.cos(angle),np.sin(angle)],[-np.sin(angle),np.cos(angle)]])
B = np.dot(R_rt,np.array([[width/2], [height/2]])) + center

R_rb = np.array([[-np.cos(angle),np.sin(angle)],[np.sin(angle),np.cos(angle)]])
C = np.dot(R_rb,np.array([[width/2], [height/2]])) + center

R_lb = np.array([[-np.cos(angle),-np.sin(angle)],[np.sin(angle),-np.cos(angle)]])
D = np.dot(R_lb,np.array([[width/2], [height/2]])) + center

corners = [A,B,C,D]

print(corners)