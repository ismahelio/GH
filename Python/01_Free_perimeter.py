

__author__ = "ismael.sanz"
__version__ = "2020.02.11"

import rhinoscriptsyntax as rs
from random import choice, uniform

start_y = point.Y
point_0 = point

limit = point.X + length
print limit
z_axis = rs.CreateVector(0,0,1)

detail = 10


x_mov = rs.CreateVector(detail,0,0)

go_bool = [True, True, True, True, False]

pts = []


while point.X<limit:
    go = choice(go_bool)
    if go:
        pass
    else:
        angle = -5
        while angle<0:
            rotation = uniform(90,-90)
            temp_mov = rs.VectorRotate(x_mov, rotation, z_axis)
            new_pt = rs.CopyObject(point, temp_mov)
            new_pt = rs.coerce3dpoint(new_pt)
            angle = new_pt.X - point.X
        x_mov = temp_mov
    point = rs.CopyObject(point, x_mov)
    
    pts.append(point)
    point = rs.coerce3dpoint(point)

limit = point.Y + length

x_mov = rs.CreateVector(0,detail,0)
while point.Y<limit:
    go = choice(go_bool)
    if go:
        pass
    else:
        angle = -5
        while angle<0:
            rotation = uniform(90,-90)
            temp_mov = rs.VectorRotate(x_mov, rotation, z_axis)
            new_pt = rs.CopyObject(point, temp_mov)
            new_pt = rs.coerce3dpoint(new_pt)
            angle = new_pt.Y - point.Y
        x_mov = temp_mov
    point = rs.CopyObject(point, x_mov)
    
    pts.append(point)
    point = rs.coerce3dpoint(point)
    

limit = point.X - length

x_mov = rs.CreateVector(-detail,0,0)
while point.X>limit:
    go = choice(go_bool)
    if go:
        pass
    else:
        angle = -5
        while angle<0:
            rotation = uniform(90,-90)
            temp_mov = rs.VectorRotate(x_mov, rotation, z_axis)
            new_pt = rs.CopyObject(point, temp_mov)
            new_pt = rs.coerce3dpoint(new_pt)
            angle = point.X - new_pt.X  
        x_mov = temp_mov
    point = rs.CopyObject(point, x_mov)
    
    pts.append(point)
    point = rs.coerce3dpoint(point)



# Last direction

vector_x = rs.VectorCreate(point, point_0)
dist_pts = rs.Distance(point, point_0)

pt_start_last = point

go_bool = ["rotate", "same", "go_to_origin"]


x_vec = rs.VectorUnitize(vector_x)
count = 0
count2 = 0
while dist_pts > 20:
    go = choice(go_bool)
    print go
    if go == "same":
        pass
    if go == "rotate":
        angle = -5
        while angle < 45:
            
            
            rotation = uniform(90,-90)
            temp_mv = rs.VectorRotate(x_vec, rotation, z_axis)
            new_pt = rs.CopyObject(point, temp_mv)
            new_pt = rs.coerce3dpoint(new_pt)
            
            v2 = rs.VectorCreate(new_pt, pt_start_last)
            
            angle = rs.VectorAngle(vector_x, v2)
            
            count2+=1
            if count2 == 100:
                break
                print "break"
                
        count2 = 0
        x_vec = rs.VectorUnitize(temp_mv) * detail
    if go == "go_to_origin":
        x_vec = rs.VectorCreate(point_0, point)
        x_vec = rs.VectorUnitize(x_vec) * detail
    
    point = rs.CopyObject(point, x_vec)
    pts.append(point)
    point = rs.coerce3dpoint(point)
    
    dist_pts = rs.Distance(point, point_0)
    
    print dist_pts
    count+=1
    if count == 1000:
        break
