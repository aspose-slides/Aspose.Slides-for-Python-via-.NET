import aspose.slides as slides


#ExStart:CloneToAnotherPresentationWithMaster
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Instantiate Presentation class to load the source presentation file

with slides.Presentation(dataDir + "welcome-to-powerpoint.pptx") as srcPres:
    # Instantiate Presentation class for destination presentation (where slide is to be cloned)
    with slides.Presentation() as destPres:
        # Instantiate from the collection of slides in source presentation along with
        # Master slide
        srcSlide = srcPres.slides[0]
        srcMaster = srcSlide.layout_slide.master_slide

        # Clone the desired master slide from the source presentation to the collection of masters in the
        # Destination presentation
        masters = destPres.masters
        DestMaster = srcSlide.layout_slide.master_slide

        # Clone the desired master slide from the source presentation to the collection of masters in the
        # Destination presentation
        iSlide = masters.add_clone(srcMaster)

        # Clone the desired slide from the source presentation with the desired master to the end of the
        # Collection of slides in the destination presentation
        slds = destPres.slides
        slds.add_clone(srcSlide, iSlide, True)
        
        # Clone the desired master slide from the source presentation to the collection of masters in the # Destination presentation
        # Save the destination presentation to disk
        destPres.save(outDir + "crud_clone_with_master_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:CloneToAnotherPresentationWithMaster