import aspose.slides as slides

def convert_to_pdf_hidden_slides():
    #ExStart:ConvertToPDFWithHiddenSlides
    # The path to the documents directory.
    dataDir = "./examples/data/"
    outDir = "./examples/out/"
    with slides.Presentation(dataDir + "presentation_with_hidden_slides.pptx") as presentation:
        # Instantiate the PdfOptions class
        pdfOptions = slides.export.PdfOptions()

        # Specify that the generated document should include hidden slides
        pdfOptions.show_hidden_slides = True

        # Save the presentation to PDF with specified options
        presentation.save(outDir + "convert_to_pdf_hidden_slides_out.pdf", slides.export.SaveFormat.PDF, pdfOptions)
    #ExEnd:ConvertToPDFWithHiddenSlides

