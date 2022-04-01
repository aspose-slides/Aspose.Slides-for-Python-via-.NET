import aspose.slides as slides

def convert_to_pdf_custom_options():
    #ExStart:CustomOptionsPDFConversion
    # The path to the documents directory.
    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    # Instantiate a Presentation object that represents a presentation file
    with slides.Presentation(dataDir + "welcome-to-powerpoint.pptx") as pres:
        # Instantiate the PdfOptions class
        pdfOptions = slides.export.PdfOptions()

        # Set Jpeg Quality
        pdfOptions.jpeg_quality = 90

        # Define behavior for metafiles
        pdfOptions.save_metafiles_as_png = True

        # Set Text Compression level
        pdfOptions.text_compression = slides.export.PdfTextCompression.FLATE

        # Define the PDF standard
        pdfOptions.compliance = slides.export.PdfCompliance.PDF15


        options = pdfOptions.notes_comments_layouting
        options.notes_position = slides.export.NotesPositions.BOTTOM_FULL

        # Save the presentation to PDF with specified options
        pres.save(outDir + "convert_to_pdf_custom_options_out.pdf", slides.export.SaveFormat.PDF, pdfOptions)
    #ExEnd:CustomOptionsPDFConversion