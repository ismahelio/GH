## Introduce a list of curves and returns the same list without duplicated ones
##INPUT
    ## crvs (List Access / Curve)
##OUTPUT
    ## crvs



import rhinoscriptsyntax as rs
import scriptcontext as sc


numbers=[]
x=crvs

def puntos_magicos(curva):
    #Pilla los puntos de una curva y suma todos su valores
    points=[]
    number = 0
    points_to_check=rs.CurvePoints(curva)
    for i in range(len(points_to_check)):
        id=sc.doc.Objects.AddPoint(points_to_check[i])
        coor=rs.PointCoordinates(id)
        number+=sum(coor)
        #Mete el numero final en una lista
    number=round(number,5)
    numbers.append(number)


#Asigna valores a las curvas
for i in range(len(x)):
    puntos_magicos(x[i])


numbers_f=[]
crvs=[]


if not numbers[0] in numbers_f:
    print 'HOLA'



for i in range(len(x)):
    #Si el numero no esta en la lista numbers_f: metemos curvas en la crvs
    if not numbers[i] in numbers_f:
        numbers_f.append(numbers[i])
        crvs.append(x[i])


print numbers_f
