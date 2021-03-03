import Rhino
import os
import rhinoscriptsyntax as rs

new3dm = Rhino.FileIO.File3dm()

#Properties of geometry 1
attributes = Rhino.DocObjects.ObjectAttributes()
attributes.LayerIndex = 0;
attributes.Name = "geo"
attributes.ObjectColor = c1
attributes.ColorSource = Rhino.DocObjects.ObjectColorSource.ColorFromObject

#Properties of geometry 2
attributes_text = Rhino.DocObjects.ObjectAttributes()
attributes_text.LayerIndex = 0;
attributes_text.Name = "text"
attributes_text.ObjectColor = c2
attributes_text.ColorSource = Rhino.DocObjects.ObjectColorSource.ColorFromObject

for c in crv:
    #Curve
    new3dm.Objects.AddCurve(c, attributes)

for t,p,h,j in zip(T,P,H,J): 
    #Text
    new3dm.Objects.AddText(t, p, h, "Arial", False, False, j, attributes_text)

for d in dim:
    #Dimensions
    new3dm.Objects.AddLinearDimension(d, attributes_text)



if write:
    filename = 'layout.3dm'
    path = os.path.join(t_path, filename)
    new3dm.Write(path,6)

