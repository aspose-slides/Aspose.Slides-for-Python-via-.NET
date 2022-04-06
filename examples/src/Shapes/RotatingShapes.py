import aspose.slides as slides

#ExStart:RotatingShapes
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Instantiate Presentation class that represents the PPTX
with slides.Presentation() as pres:
    # Get the first slide
    sld = pres.slides[0]

    # Add autoshape of rectangle type
    shp = sld.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 50, 150, 75, 150)

    # Rotate the shape to 90 degree
    shp.rotation = 90

    # Write the PPTX file to disk
    pres.save(outDir + "shapes_rotate_out.pptx", slides.export.SaveFormat.PPTX)

#ExEnd:RotatingShapes