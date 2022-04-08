import aspose.slides as slides

#ExStart:CreateGroupShape
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Instantiate Prseetation class 
with slides.Presentation() as pres:
    # Get the first slide 
    sld = pres.slides[0]

    # Accessing the shape collection of slides 
    slideShapes = sld.shapes

    # Adding a group shape to the slide 
    groupShape = slideShapes.add_group_shape()

    # Adding shapes inside added group shape 
    groupShape.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 300, 100, 100, 100)
    groupShape.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 500, 100, 100, 100)
    groupShape.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 300, 300, 100, 100)
    groupShape.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 500, 300, 100, 100)

    # Adding group shape frame 
    groupShape.frame = slides.ShapeFrame(100, 300, 500, 40, -1, -1, 0)

    # Write the PPTX file to disk 
    pres.save(outDir + "shapes_create_group_shape_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:CreateGroupShape
