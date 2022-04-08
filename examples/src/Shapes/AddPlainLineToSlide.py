import aspose.slides as slides

#ExStart:AddPlainLineToSlide
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Instantiate Presentation class that represents the PPTX file
with slides.Presentation() as pres:
    # Get the first slide
    sld = pres.slides[0]

    # Add an autoshape of type line
    sld.shapes.add_auto_shape(slides.ShapeType.LINE, 50, 150, 300, 0)

    #Write the PPTX to Disk
    pres.save(outDir + "shapes_add_plain_line_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:AddPlainLineToSlide