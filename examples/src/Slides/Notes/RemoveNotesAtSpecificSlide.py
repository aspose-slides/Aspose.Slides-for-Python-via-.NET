import aspose.slides as slides


# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

#ExStart:RemoveNotesAtSpecificSlide
# Instantiate a Presentation object that represents a presentation file 
with slides.Presentation(dataDir + "welcome-to-powerpoint.pptx") as presentation:

    # Removing notes of first slide
    mgr = presentation.slides[0].notes_slide_manager
    mgr.remove_notes_slide()

    # Save presentation to disk
    presentation.save(outDir + "notes_remove_notes_slide_out.pptx", slides.export.SaveFormat.PPTX)

#ExEnd:RemoveNotesAtSpecificSlide