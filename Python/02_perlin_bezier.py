# input n_div (int)
# input n_segments (int)

__author__ = "ismael.sanz"
__version__ = "2020.03.02"

from random import uniform

#defines 50% of the bezier curve
def bezier(x, u0, u1, u2, u3):
    step1 = u0*(1-x)**3
    step2 = 3*u1*((1-x)**2)*x
    step3 = 3*u2*(1-x)*x**2
    step4 = u3*x**3
    
    y = step1 + step2 + step3 + step4
    
    return y



def bezier_values(n_div):
    y = []
    y_reverse = []
    for i in range(n_div):
        y.append(bezier(i, 0, 0.05, 0.25, 1))
        y_reverse.append(bezier(i, 0, 0.05, 0.25, 1))
        
    
    
    height = y[-1] * 2
    y_reverse.reverse()
    
    del y[-1]
    
    for i in range(n_div):
        y.append(height - y_reverse[i])
    
    y_remap = []
    for value in y:
        OldMin = 0
        NewMin = 0
        OldMax = y[-1]
        NewMax = 1
        
        NewValue = (((value - OldMin) * (NewMax - NewMin)) / (OldMax - OldMin)) + NewMin
        y_remap.append(NewValue)
    
    return y_remap



y_value = 0

# y values of the function
ys = []
# x values of the function
xs = []



# It creates the number of points as input: max_pts

# Change n_div for the number of division per curve
# Change y_int as the intensity of y values 

adding_points = True

j = 0

while adding_points:
    
    n_div = uniform(7,20)
    
    n_div = int(n_div)
    y = bezier_values(n_div)
    
    
    x_int = 1
    y_int = uniform(10,50)
    
    if j%2 == 0:
        for i in range(len(y)):
            y_ = y_value + (y[i] * y_int)
            ys.append(y_)
            xs.append(x_int)
            
            if len(ys)==max_pts:
                adding_points = False
                break
            
            
        y_value = y_
    else:
        for i in range(len(y)):
            y_ = y_value - (y[i] * y_int)
            ys.append(y_)
            xs.append(x_int)
            if len(ys)==max_pts:
                adding_points = False
                break
        y_value = y_
    
    j+=1


