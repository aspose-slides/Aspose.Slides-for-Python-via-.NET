import aspose.slides as slides

def convet_to_swf():
    #ExStart:ConvetToSWF
    # The path to the documents directory.
    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    # Instantiate a Presentation object that represents a presentation file
    with slides.Presentation(dataDir + "welcome-to-powerpoint.pptx") as presentation:
        swfOptions = slides.export.SwfOptions()
        swfOptions.viewer_included = False


        notesOptions = swfOptions.notes_comments_layouting
        notesOptions.notes_position = slides.export.NotesPositions.BOTTOM_FULL

        # Saving presentation and notes pages
        presentation.save(outDir + "convet_to_swf_out.swf", slides.export.SaveFormat.SWF, swfOptions)

        swfOptions.viewer_included = True
        presentation.save(outDir + "convet_to_swf_with_notes_out.swf", slides.export.SaveFormat.SWF, swfOptions)
    #ExEnd:ConvetToSWF
