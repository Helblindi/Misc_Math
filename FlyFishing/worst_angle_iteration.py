import numpy as np
from point import *
from useful_functions import *

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

def main():
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

    iterations = 0
    # while get_average_difference_in_angle(points) > 5:
    for i in range(0, 7):
        iterations += 1
        avg_ang = get_average_angle(points)

        # generate list of current angles
        current_angles = []
        for i in range(1, len(points) - 1):
            angle = get_angle(points[i - 1], points[i], points[i + 1])
            current_angles.append(angle)

        difference_in_angles = []
        for i in current_angles:
            difference_in_angles.append(np.abs(avg_ang - i))

        print('avg ang: ', avg_ang)
        print('current angles: ', current_angles)
        print('difference: ', difference_in_angles)
        print('max: ', max(difference_in_angles))
        index = difference_in_angles.index(max(difference_in_angles))
        print('index: ', index)
        print_points_set(points)

        # run algorithm on position with greatest difference in angle from the average
        possible_x_vals = np.linspace(points[index].x, points[index + 2].x, 50, endpoint=False)
        possible_x_vals = np.delete(possible_x_vals, 0)

        # generate list of possible points from previously generated x_vals
        possible_points = []
        for x in possible_x_vals:
            possible_points.append(Point(x, fun(x)))

        # generate list of possible angles from previously generated points
        possible_angles = []
        possible_ang_dif = []
        for possible_point in possible_points:
            angle = get_angle(points[index], possible_point, points[index + 2])
            possible_angles.append(angle)
            possible_ang_dif.append(np.abs(angle - avg_ang))

        new_x_index = np.argmin(possible_ang_dif)
        new_x = possible_x_vals[new_x_index]
        points[index + 1] = Point(new_x, fun(new_x))

        print('+++++++++++++ AVERAGE: ', get_average_difference_in_angle(points))
        plot_points_and_function(fun, points)

    print('found in iterations: ', iterations)

    return 0

# While not required, it is considered good practice to have
# a main function and use this syntax to call it.
if __name__ == "__main__":
    main()
