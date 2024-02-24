import aspose.slides as slides


def convert_to_pdf_notes(global_opts):
    # Instantiate a Presentation object that represents a presentation file
    with slides.Presentation(global_opts.data_dir + "welcome-to-powerpoint.pptx") as presentation, \
            slides.Presentation() as aux_presentation:
        slide = presentation.slides[0]

        aux_presentation.slides.insert_clone(0, slide)

        # Setting Slide Type and Size
        # aux_presentation.slide_size.set_size(presentation.slide_size.size.width, presentation.slide_size.size.height,slides.SlideSizeScaleType.ENSURE_FIT)
        aux_presentation.slide_size.set_size(612, 792, slides.SlideSizeScaleType.ENSURE_FIT)

        pdf_options = slides.export.PdfOptions()
        options = pdf_options.notes_comments_layouting
        options.notes_position = slides.export.NotesPositions.BOTTOM_FULL

        aux_presentation.save(global_opts.out_dir + "convert_to_pdf_notes_out.pdf", slides.export.SaveFormat.PDF,
                              pdf_options)
