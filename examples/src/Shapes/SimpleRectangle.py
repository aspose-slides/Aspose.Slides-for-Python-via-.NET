import aspose.slides as slides

#ExStart:SimpleRectangle
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Instantiate Prseetation class that represents the PPTX
with slides.Presentation() as pres:
    # Get the first slide
    sld = pres.slides[0]

    # Add autoshape of rectangle type
    sld.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 50, 150, 150, 50)

    #Write the PPTX file to disk
    pres.save(outDir+ "shapes_add_rectangle_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:SimpleRectangle