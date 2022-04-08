import aspose.slides as slides


#ExStart:CloneWithinSamePresentationToEnd
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Instantiate Presentation class that represents a presentation file
with slides.Presentation(dataDir + "welcome-to-powerpoint.pptx") as pres:
    # Clone the desired slide to the end of the collection of slides in the same presentation
    slds = pres.slides

    slds.add_clone(pres.slides[0])

    # Write the modified presentation to disk
    pres.save(outDir + "crud_add_clone3_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:CloneWithinSamePresentationToEnd