import aspose.slides as slides


#ExStart:ChangePosition
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Instantiate Presentation class to load the source presentation file
with slides.Presentation(dataDir + "welcome-to-powerpoint.pptx") as pres:
    # Get the slide whose position is to be changed
    sld = pres.slides[0]

    # Set the new position for the slide
    sld.slide_number = 2

    # Write the presentation to disk
    pres.save(outDir + "crud_change_position_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:ChangePosition