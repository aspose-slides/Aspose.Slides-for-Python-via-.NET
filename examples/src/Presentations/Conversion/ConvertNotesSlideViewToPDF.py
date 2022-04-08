import aspose.slides as slides

def convert_notes_to_pdf():
    #ExStart:ConvertNotesSlideViewToPDF
    # The path to the documents directory.
    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    # Instantiate a Presentation object that represents a presentation file
    with slides.Presentation(dataDir + "presentation_with_notes.pptx") as presentation:
        pdfOptions = slides.export.PdfOptions()
        options = pdfOptions.notes_comments_layouting
        options.notes_position = slides.export.NotesPositions.BOTTOM_FULL

        
        # Saving the presentation to PDF notes
        presentation.save(outDir + "convert_notes_to_pdf_out.pdf", slides.export.SaveFormat.PDF, pdfOptions)
    #ExEnd:ConvertNotesSlideViewToPDF
