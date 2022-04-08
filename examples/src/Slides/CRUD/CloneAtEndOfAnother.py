import aspose.slides as slides

#ExStart:CloneAtEndOfAnother
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Instantiate Presentation class to load the source presentation file
with slides.Presentation(dataDir + "welcome-to-powerpoint.pptx") as srcPres:
    # Instantiate Presentation class for destination PPTX (where slide is to be cloned)
    with slides.Presentation() as destPres:
        # Clone the desired slide from the source presentation to the end of the collection of slides in destination presentation
        slds = destPres.slides

        slds.add_clone(srcPres.slides[0])

        # Write the destination presentation to disk
        destPres.save(outDir + "crud_add_clone_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:CloneAtEndOfAnother