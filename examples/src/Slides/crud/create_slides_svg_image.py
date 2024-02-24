import aspose.slides as slides


def create_slides_svg_image(global_opts):
    # Instantiate a Presentation class that represents the presentation file
    with slides.Presentation(global_opts.data_dir + "welcome-to-powerpoint.pptx") as pres:
        # Access the first slide
        all_slides = pres.slides[0]

        # Create a memory stream object
        with open(global_opts.out_dir + "crud_save_as_svg_out.svg", "wb") as stream:
            all_slides.write_as_svg(stream)
