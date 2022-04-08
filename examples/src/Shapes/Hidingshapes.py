import aspose.slides as slides
            
#ExStart:Hidingshapes
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Instantiate Presentation class that represents the PPTX
with slides.Presentation() as pres:
    # Get the first slide
    sld = pres.slides[0]

    # Add autoshape of rectangle type
    shp1 = sld.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 50, 40, 150, 50)
    shp2 = sld.shapes.add_auto_shape(slides.ShapeType.MOON, 160, 40, 150, 50)
    alttext = "User Defined"

    for shape in sld.shapes:
        if shape.alternative_text == alttext:
                shape.hidden = True

    # Save presentation to disk
    pres.save(outDir + "shapes_hide_shape_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:Hidingshapes


