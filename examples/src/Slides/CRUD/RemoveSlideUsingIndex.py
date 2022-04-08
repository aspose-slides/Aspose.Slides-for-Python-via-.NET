import aspose.slides as slides


#ExStart:RemoveSlideUsingIndex
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Instantiate a Presentation object that represents a presentation file
with slides.Presentation(dataDir + "welcome-to-powerpoint.pptx") as pres:
    # Removing a slide using its slide index
    pres.slides.remove_at(0)

    # Writing the presentation file
    pres.save(outDir + "crud_remove_at_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:RemoveSlideUsingIndex