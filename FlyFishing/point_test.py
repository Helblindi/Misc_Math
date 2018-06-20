from point import *

# Examples of how to use the point class

p1 = Point(3, 4)

p2 = Point(10, 20)

print('\np1 = ', p1) # uses __str__ if defined

print('\np2 = ', p2)
print(str(p2))

# without __str__ defined, str(p1) would print something like
# <__main__.Point object at 0x1007a2050>.  That is, Python language tries to
# print as much as it knows about the object as a printed representation.

print('\nPoint.__doc__ =')
print(Point.__doc__)

# This computes the distance from the origin to p1.
print('\np1.distance_from_origin() =', p1.distance_from_origin())

# This one between p1 and p2.
print('\np1.distance(p2) =', p1.distance(p2))

# Add two points
print('\np1.__add__(p2) =', p1.__add__(p2))
print(p1 + p2)

print("\np2.__cmp__(p1) = ", p2.__cmp__(p1))

print('\nPoint.points-------------', Point.points)


# ===========================================================================
# Set of objects
#
# Once we know how to create objects, we would probably want to deal with
# a collection of objects as we try to write interesting programs.  For
# example, we may want to create a list of point objects and deal with
# the list to find the points that are within a certain distance from the
# origin, say.

# Creates a list of point objects, m * n of them:
#
def create_points_set(m, n):
    points = []
    i = 0
    while i < m:
        # print 'i = ' + str(i)
        j = 0
        while j < n:
            # print '   j = ' + str(j)
            points.append(Point(i, j))
            j = j + 1
        i = i + 1
    return points


# Use the function to create a list:
ps = create_points_set(2, 3)


# Once you create a list, you can do whatever you want to do with it.  Here,
# print each by using a function:

def print_points_set(points):
    for p in points:
        print(p)


print('\nprint_points_set(ps) =', print_points_set(ps))


# Find points within a certain distance from the origin
def find_points_within(points, d):
    ps = []
    for p in points:
        # print p.distance_from_origin()
        if p.distance_from_origin() < d:
            ps.append(p)
    return ps


print('\nprint_points_set(find_points_within(ps, 2)) =', print_points_set(find_points_within(ps, 2)))
