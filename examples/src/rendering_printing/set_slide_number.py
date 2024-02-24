import aspose.slides as slides


def rendering_set_slide_number(global_opts):
    # Instantiate a Presentation object that represents a presentation file
    with slides.Presentation(global_opts.data_dir + "welcome-to-powerpoint.pptx") as presentation:
        # Get the slide number
        first_slide_number = presentation.first_slide_number

        # Set the slide number
        presentation.first_slide_number = 10

        presentation.save(global_opts.out_dir + "rendering_set_slide_number_out.pptx", slides.export.SaveFormat.PPTX)
