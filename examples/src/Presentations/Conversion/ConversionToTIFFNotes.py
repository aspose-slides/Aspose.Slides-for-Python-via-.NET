import aspose.slides as slides

def convert_to_tiff_notes():
    #ExStart:ConversionToTIFFNotes
    # The path to the documents directory.
    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    # Instantiate a Presentation object that represents a presentation file
    with slides.Presentation(dataDir + "presentation_with_notes.pptx") as presentation:
        # Saving the presentation to TIFF notes
        presentation.save(outDir + "convert_to_tiff_notes_out.tiff", slides.export.SaveFormat.TIFF)
    #ExEnd:ConversionToTIFFNotes
