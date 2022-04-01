import aspose.slides as slides

def convert_to_password_protected_pdf():
    #ExStart:ConvertPresentationToPasswordProtectedPDF
    # The path to the documents directory.
    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    # Instantiate a Presentation object that represents a presentation file
    with slides.Presentation(dataDir + "welcome-to-powerpoint.pptx") as presentation:
        # Instantiate the PdfOptions class
        pdfOptions = slides.export.PdfOptions()

        # Setting PDF password
        pdfOptions.password = "password"

        # Save the presentation to password protected PDF
        presentation.save(outDir + "convert_to_password_protected_pdf_out.pdf", slides.export.SaveFormat.PDF, pdfOptions)
    #ExEnd:ConvertPresentationToPasswordProtectedPDF
    
