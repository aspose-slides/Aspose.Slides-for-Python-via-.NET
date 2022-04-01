import aspose.slides as slides

def convert_specific_slide_to_pdf():
    #ExStart:ConvertSpecificSlideToPDF
    # The path to the documents directory.
    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    # Instantiate a Presentation object that represents a presentation file
    with slides.Presentation(dataDir + "welcome-to-powerpoint.pptx") as presentation:
        # Setting array of slides positions
        indexes = [ 1, 3 ]

        # Save the presentation to PDF
        presentation.save(outDir + "convert_specific_slide_to_pdf_out.pdf", indexes, slides.export.SaveFormat.PDF)
    #ExEnd:ConvertSpecificSlideToPDF
