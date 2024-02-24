import aspose.slides as slides


def set_size_and_type(global_opts):
    # Instantiate a Presentation object that represents a presentation file
    with slides.Presentation(global_opts.data_dir + "welcome-to-powerpoint.pptx") as presentation:
        with slides.Presentation() as aux_presentation:
            slide = presentation.slides[0]

            # Set the slide size of generated presentations to that of source
            aux_presentation.slide_size.set_size(presentation.slide_size.type, slides.SlideSizeScaleType.ENSURE_FIT)

            aux_presentation.slides.insert_clone(0, slide)
            aux_presentation.slides.remove_at(0)
            # Save Presentation to disk
            aux_presentation.save(global_opts.out_dir + "layout_slide_size_out.pptx", slides.export.SaveFormat.PPTX)
