import aspose.slides as slides


def convert_to_pdf_custom_options(global_opts):
    # Instantiate a Presentation object that represents a presentation file
    with slides.Presentation(global_opts.data_dir + "welcome-to-powerpoint.pptx") as pres:
        # Instantiate the PdfOptions class
        pdf_options = slides.export.PdfOptions()

        # Set Jpeg Quality
        pdf_options.jpeg_quality = 90

        # Define behavior for metafiles
        pdf_options.save_metafiles_as_png = True

        # Set Text Compression level
        pdf_options.text_compression = slides.export.PdfTextCompression.FLATE

        # Define the PDF standard
        pdf_options.compliance = slides.export.PdfCompliance.PDF15

        notes_comments_layouting_options = pdf_options.notes_comments_layouting
        notes_comments_layouting_options.notes_position = slides.export.NotesPositions.BOTTOM_FULL

        # Save the presentation to PDF with specified options
        pres.save(global_opts.out_dir + "convert_to_pdf_custom_options_out.pdf", slides.export.SaveFormat.PDF,
                  pdf_options)
