import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize


########################################################################################################################
#  Useful Functions
########################################################################################################################

# Useful functions for creating a list of points
def print_points_set(points):
    for p in points:
        print(p)

# get the x intercept of the function
def get_x_int(fun):
    x0 = np.array([30])
    sol = optimize.root(fun, x0, method='hybr')
    x_int = sol.x
    return x_int

# function to get the average of the difference of angles for the average of the angles
def get_average_difference_in_angle(points):
    avg_ang = get_average_angle(points)
    sum = 0
    for i in range(1, len(points) - 1):
        angle = get_angle(points[i-1], points[i], points[i+1])
        sum += np.abs(avg_ang - angle)

    avg = sum / len(points)
    return avg

# function to return the coordinate values of the points
def get_coordinate_values(points):
    x_coords = []
    y_coords = []
    for point in points:
        x, y = point.separate()
        x_coords.append(x)
        y_coords.append(y)
    return x_coords, y_coords

# function to seamlessly plot a given function and points
def plot_points_and_function(fun, points):
    x_int = get_x_int(fun)
    x_vals, y_vals = get_coordinate_values(points)
    plt.plot(x_vals, y_vals, 'r-')
    x = np.linspace(0, x_int, 100)
    plt.plot(x, fun(x), 'b-')
    plt.show()

# function to get the average angles across the points, not including the end points
def get_average_angle(points):
    angles = []
    # iterate through all left endpoints of angles
    for i in range(0, len(points) - 2):
        angles.append(get_angle(points[i], points[i+1], points[i+2]))

    # now that we have an array of our angles, calculate the average
    sum = 0
    for i in angles:
        sum += i

    avg = sum / len(angles)
    return avg

# function to return the vectors given magnitude
def mag_vec(v):
    return v.distance_from_origin()

# function to get the angle between three points
def get_angle(point_1, point_2, point_3):
    v1 = point_1 - point_2
    v2 = point_3 - point_2

    val = (v1 * v2) / (mag_vec(v1) * mag_vec(v2))
    ang = np.arccos(val)
    ang = ang * 180 / np.pi
    return ang

########################################################################################################################
#  END Useful Functions
########################################################################################################################
