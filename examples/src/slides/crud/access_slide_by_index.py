import aspose.slides as slides


def access_slide_by_index(global_opts):
    # Create an instance of Presentation class
    with slides.Presentation(global_opts.data_dir + "welcome-to-powerpoint.pptx") as presentation:
        # Obtain a slide's reference by its index
        slide = presentation.slides[0]
