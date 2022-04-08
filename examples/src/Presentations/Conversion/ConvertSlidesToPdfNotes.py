import aspose.pydrawing as drawing
import aspose.slides as slides

def convert_to_pdf_notes():
    #ExStart:ConvertSlidesToPdfNotes
    # The path to the documents directory.
    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    # Instantiate a Presentation object that represents a presentation file 
    with slides.Presentation(dataDir + "welcome-to-powerpoint.pptx") as presentation:
        with slides.Presentation() as auxPresentation:
            slide = presentation.slides[0]

            auxPresentation.slides.insert_clone(0, slide)

            # Setting Slide Type and Size 
            #auxPresentation.slide_size.set_size(presentation.slide_size.size.width, presentation.slide_size.size.height,slides.SlideSizeScaleType.ENSURE_FIT)
            auxPresentation.slide_size.set_size(612, 792, slides.SlideSizeScaleType.ENSURE_FIT)


            pdfOptions = slides.export.PdfOptions()
            options = pdfOptions.notes_comments_layouting
            options.notes_position = slides.export.NotesPositions.BOTTOM_FULL

            auxPresentation.save(outDir + "convert_to_pdf_notes_out.pdf", slides.export.SaveFormat.PDF, pdfOptions)
    #ExEnd:ConvertSlidesToPdfNotes
