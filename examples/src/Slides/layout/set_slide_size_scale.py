import aspose.slides as slides


def set_slide_size_scale(global_opts):
    # Instantiate a Presentation object that represents a presentation file
    with slides.Presentation(global_opts.data_dir + "welcome-to-powerpoint.pptx") as presentation:
        with slides.Presentation() as aux_presentation:
            slide = presentation.slides[0]

            # Set the slide size of generated presentations to that of source
            presentation.slide_size.set_size(540, 720, slides.SlideSizeScaleType.ENSURE_FIT)
            # Method SetSize is used for set slide size with scale content to ensure fit
            presentation.slide_size.set_size(slides.SlideSizeType.A4_PAPER, slides.SlideSizeScaleType.MAXIMIZE)
            # Method SetSize is used for set slide size with maximize size of content

            # Save Presentation to disk
            aux_presentation.save(global_opts.out_dir + "layout_slide_size_scale_out.pptx",
                                  slides.export.SaveFormat.PPTX)
