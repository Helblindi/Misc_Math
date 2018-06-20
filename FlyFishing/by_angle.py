import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
from point import *

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
    plt.plot(x_vals, y_vals, 'ro')
    plt.axis('scaled')
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

########################################################################################################################
#  Parameters
########################################################################################################################

"""
Echo_1
"""
def fun(x):
    return .0571 + 3.58 * x - 0.473 * x**2 + 0.0345 * x**3 - .00141 \
           * x**4 + .0000291 * x**5 - .000000239 * x**6

"""
Echo_2
"""
# def fun(x):
#     return 3.02 + 2.74 * x - 0.273 * x**2 + 0.0156 * x**3 - 0.00052 \
#            * x**4 + 0.00000879 * x**5 - 0.0000000589 * x**6

########################################################################################################################
#  END Parameters
########################################################################################################################

# get x intercept
x_int = get_x_int(fun)

# partition the interval for the initial positions
# assuming x = 0 is the first guide ring location
rings = int(input("How many rings?"))
x_vals = np.linspace(0, x_int, rings)

# create a list of Points where each ring is located
points = []
for x in x_vals:
    points.append(Point(x, fun(x)))

# print('before')
print(print_points_set(points))
# first get the average angle

iterations = 0
while get_average_difference_in_angle(points) > 5:
    iterations += 1
    avg_ang = get_average_angle(points)
    plot_points_and_function(fun, points)
    print('avg ang: ', avg_ang)

    # run algorithm on each position iteratively till a tolerance is reached
    for i in range(1, len(points) - 1):
        # generate list of x_vals based on previous and next guide ring
        # note that we cannot have either the first or the last x value in this
        # interval, otherwise our angle values will be null
        # print('\nCurrent interval is between ')
        # print(points[i-1].x)
        # print(' and ')
        # print(points[i+1].x)

        avg_ang = get_average_angle(points)

        possible_x_vals = np.linspace(points[i-1].x, points[i+1].x, 50, endpoint=False)
        possible_x_vals = np.delete(possible_x_vals, 0)

        # generate list of possible points from previously generated x_vals
        possible_points = []
        for x in possible_x_vals:
            possible_points.append(Point(x, fun(x)))

        # generate list of possible angles from previously generated points
        possible_angles = []
        possible_ang_dif = []
        for possible_point in possible_points:
            angle = get_angle(points[i-1], possible_point, points[i+1])
            possible_angles.append(angle)
            possible_ang_dif.append(np.abs(angle - avg_ang))

        new_x_index = np.argmin(possible_ang_dif)
        new_x = possible_x_vals[new_x_index]
        points[i] = Point(new_x, fun(new_x))

        # print('\npoint: ', i)
        # print('possible angles: ', possible_angles)
        # print('angle: ', possible_angles[int(new_x_index)])
        # print('difference from average: ', possible_ang_dif[int(new_x_index)])

    avg_ang = get_average_angle(points)
    # print('avg ang: ', avg_ang)
    print('+++++++++++++ AVERAGE: ', get_average_difference_in_angle(points))

print('found in iterations: ', iterations)
