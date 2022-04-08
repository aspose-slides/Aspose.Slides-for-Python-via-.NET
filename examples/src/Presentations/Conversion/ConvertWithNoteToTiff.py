import aspose.slides as slides

def convert_to_tiff_with_notes():
    #ExStart:ConvertWithNoteToTiff
    # The path to the documents directory.
    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    # Instantiate a Presentation object that represents a presentation file
    with slides.Presentation(dataDir + "presentation_with_notes.pptx") as pres:
        opts = slides.export.TiffOptions()
        notesOptions = opts.notes_comments_layouting
        notesOptions.notes_position = slides.export.NotesPositions.BOTTOM_FULL
        # Saving the presentation to TIFF notes
        pres.save(outDir + "convert_to_tiff_with_notes_out.tiff", slides.export.SaveFormat.TIFF, opts)
    #ExEnd:ConvertWithNoteToTiff