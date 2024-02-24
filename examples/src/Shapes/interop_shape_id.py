import aspose.slides as slides


def interop_shape_id(global_opts):
    # Instantiate a Presentation class that represents the presentation file
    with slides.Presentation(global_opts.data_dir + "welcome-to-powerpoint.pptx") as presentation:
        # Getting unique shape identifier in slide scope
        print(str(presentation.slides[0].shapes[0].office_interop_shape_id))
