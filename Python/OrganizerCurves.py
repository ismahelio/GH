
## Appends inside the same branch Curves with data in Common
## INPUTS
    ##    crvs (List Access) 
    ##    data_in_common = the data the curves share (List Access) 
## OUTPUT
    ##    crvs


import rhinoscriptsyntax as rs
import Rhino
#import .Net CLR
import clr
#import the Grasshopper
clr.AddReference("Grasshopper")
#Import the Path and Data Tree sub-modules
from Grasshopper.Kernel.Data import GH_Path
from Grasshopper import DataTree


#Rename the variables
x=crvs
y=data_in_common

myTree = DataTree[Rhino.Geometry.Curve]()
crvs=[]


#--1. Sort the list in relation with the data_in_common
yx=[x for y, x in sorted(zip(y, x))]

x = yx

    #Give the data_in_common values back to y and sort it
y=data_in_common
y.sort()


#==Iterate through the list of points and assign them a Path value if
    #they share the same data common value


n=0
y_new=y



#Definition to select the curves inside groups
def curves_selected():
    check=y_new[0]
    for i in range(len(y)):
        if check==y_new[0]:
            mypath=GH_Path(n)
            
            pt3d=rs.coercegeometry(x[0])
            myTree.Add(pt3d,mypath)
            
            #remove the curves dispatched
            y_new.remove(y_new[0])
            x.remove(x[0])
        else:
            global n
            n=n+1
            print "Hola"
            curves_selected()
            break



curves_selected()



crvs = myTree
