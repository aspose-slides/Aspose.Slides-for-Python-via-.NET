import aspose.slides as slides


def set_pdf_page_size(global_opts):
    # Instantiate a Presentation object that represents a presentation file
    with slides.Presentation() as presentation:
        # Set SlideSize.type Property
        presentation.slide_size.set_size(slides.SlideSizeType.A4_PAPER,slides.SlideSizeScaleType.ENSURE_FIT)

        # Set different properties of PDF Options
        pdf_options = slides.export.PdfOptions()
        pdf_options.sufficient_resolution = 600

        # Save presentation to disk
        presentation.save(global_opts.out_dir + "layout_set_pdf_page_size_out.pdf", slides.export.SaveFormat.PDF, pdf_options)
