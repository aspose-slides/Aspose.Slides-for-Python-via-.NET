import aspose.slides as slides


def convert_notes_to_pdf(global_opts):
    # Instantiate a Presentation object that represents a presentation file
    with slides.Presentation(global_opts.data_dir + "presentation_with_notes.pptx") as presentation:
        pdf_options = slides.export.PdfOptions()
        options = pdf_options.notes_comments_layouting
        options.notes_position = slides.export.NotesPositions.BOTTOM_FULL

        # Saving the presentation to PDF notes
        presentation.save(global_opts.out_dir + "convert_notes_to_pdf_out.pdf", slides.export.SaveFormat.PDF, pdf_options)
