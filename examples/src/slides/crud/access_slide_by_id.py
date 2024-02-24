import aspose.slides as slides


def access_slide_by_id(global_opts):
    # Create an instance of Presentation class
    with slides.Presentation(global_opts.data_dir + "welcome-to-powerpoint.pptx") as presentation:
        # Getting Slide ID
        slide_id = presentation.slides[0].slide_id

        # Accessing Slide by ID
        slide = presentation.get_slide_by_id(slide_id)
