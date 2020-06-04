    try
    {

      // Define the doc
      RhinoDoc doc = Rhino.RhinoDoc.ActiveDoc;
      Print(doc.ToString());


      // Cast to Linear Dimension obj - or any geometry obj
      Rhino.Geometry.GeometryBase geometry = (Rhino.Geometry.GeometryBase) geo;


      // Create Layer
      Rhino.DocObjects.Layer layer = new Rhino.DocObjects.Layer();
      layer.Name = "Isma";
      // Add layer to the doc and get the index
      int layer_index = doc.Layers.Add(layer);


      //Make new attribute to set name, layer, etc
      Rhino.DocObjects.ObjectAttributes att = new Rhino.DocObjects.ObjectAttributes();
      //Add the layer by index
      att.LayerIndex = layer_index;


      // Add the obj to the doc
      doc.Objects.Add(geometry, att);

      run = true;
    }

    catch
    {
      run = false;
    }
