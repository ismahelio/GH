"""Calculates if two line segments intersect or not.
    Doesnt give the point just True or False.
    Inputs:
        pt1: (x1, y1)
        pt2: (x2, y2)
        pt3: (x3, y3)
        pt4: (x4, y4)
    Output:
        a: Boolean"""

__author__ = "ismael.sanz"
__version__ = "2020.03.04"

# Point line x start
x1 = x_start.X
y1 = x_start.Y

# Point line x end
x2 = x_end.X
y2 = x_end.Y

# Point line y start
x3 = y_start.X
y3 = y_start.Y

# Point line y end
x4 = y_end.X
y4 = y_end.Y


calc_1 = x1 * (x3 * (y2 - y4) + x4 * (y3 - y2))
calc_2 = x2 * (x3 * (y4 - y1) + x4 * (y1 - y3))
calc_3 = (x1 - x2) * (y3 - y4)
calc_4 = (x4 - x3) * (y1 - y2)

x = (calc_1 + calc_2) / (calc_3 + calc_4)


# If True the segments intersect

if x1 <= x <= x2 and x3 <= x <= x4:
    a = True
else:
    a = False
