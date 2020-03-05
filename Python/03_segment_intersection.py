""" 3 functions:
    - line_intersection = defines the intersection pt of the vectors
    - in_curves = check that the point is inside one of the lines x-y domain
    - do_lines_intersect() = checks that the pt is inside the domain of both curves
    """



__author__ = "ismael.sanz"
__version__ = "2020.03.04"



def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       raise Exception('lines do not intersect')

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    
    return (x,y)


# Check that the point is inside the x and y boundaries
def in_curve((pt1, pt2, ptx)):
    x_values = [pt1[0], pt2[0]]
    x_values.sort()
    
    x_min = x_values[0]
    x_max = x_values[1]
    
    y_values = [pt1[1], pt2[1]]
    y_values.sort()
    
    y_min = y_values[0]
    y_max = y_values[1]
    
    # Round the values in case the points are aligned but there's some minor problem with decimals
    x_min = round(x_min, 3)
    ptx_x = round(ptx[0], 3)
    x_max = round(x_max, 3)
    y_min = round(y_min, 3)
    ptx_y = round(ptx[1], 3)
    y_max = round(y_max, 3)
    
    x_in = x_min <= ptx_x <= x_max
    y_in = y_min <= ptx_y <= y_max
    
    print [x_min, ptx_x, x_max, x_in]
    print [y_min, ptx_y, y_max, y_in]
    
    if x_in and y_in:
        return True
    else:
        return False


# pts as pt1 = (x, y)
def do_lines_intersect(pt1, pt2, pt3, pt4):
    
    pt_x = line_intersection((pt1, pt2), (pt3, pt4))
    
    in_line1 = in_curve((pt1, pt2, pt_x))
    if in_line1:
        in_line2 = in_curve((pt3, pt4, pt_x))
        if in_line2:
            inside = True
        else:
            inside = False
    else:
        inside = False
    
    return [inside, pt_x]


pt1 = (x.X, x.Y)
pt2 = (y.X, y.Y)
pt3 = (z.X, z.Y)
pt4 = (u.X, u.Y)

# pt1 and pt2 from line 1
# pt3 and pt4 from line 2

# returns True or False for intersection and pt_x (pt of intersection)
inside = do_lines_intersect(pt1, pt2, pt3, pt4)

intersects = inside[0]
pt = inside[1]




