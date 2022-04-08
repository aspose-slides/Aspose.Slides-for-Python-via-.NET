import aspose.slides as slides

#ExStart:CloneAnotherPresentationAtSpecifiedPosition
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Instantiate Presentation class to load the source presentation file
with slides.Presentation(dataDir + "welcome-to-powerpoint.pptx") as sourcePresentation:
    # Instantiate Presentation class for destination presentation (where slide is to be cloned)
    with slides.Presentation() as destPres:
        # Clone the desired slide from the source presentation to the end of the collection of slides in destination presentation
        slideCollection = destPres.slides

        # Clone the desired slide from the source presentation to the specified position in destination presentation
        slideCollection.insert_clone(1, sourcePresentation.slides[1])

        # Write the destination presentation to disk
        destPres.save(outDir + "crud_insert_clone_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:CloneAnotherPresentationAtSpecifiedPosition