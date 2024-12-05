import aspose.slides as slides


def convert_notes_to_pdf(global_opts):
    # Instantiate a Presentation object that represents a presentation file
    with slides.Presentation(global_opts.data_dir + "presentation_with_notes.pptx") as presentation:
        pdf_options = slides.export.PdfOptions()
        slides_layout_options = slides.export.NotesCommentsLayoutingOptions()
        slides_layout_options.notes_position = slides.export.NotesPositions.BOTTOM_FULL
        pdf_options.slides_layout_options = slides_layout_options

        # Saving the presentation to PDF notes
        presentation.save(global_opts.out_dir + "convert_notes_to_pdf_out.pdf", slides.export.SaveFormat.PDF, pdf_options)
