import aspose.slides as slides

def convert_to_pdf():
    #ExStart:ConvertToPDF
    # The path to the documents directory.
    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    # Instantiate a Presentation object that represents a presentation file
    with slides.Presentation(dataDir + "welcome-to-powerpoint.pptx") as presentation:

        # Save the presentation to PDF with default options
        presentation.save(outDir + "convert_to_pdf_out.pdf", slides.export.SaveFormat.PDF)
    #ExEnd:ConvertToPDF    