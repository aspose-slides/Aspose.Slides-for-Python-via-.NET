import aspose.slides as slides


def change_position(global_opts):
    # Instantiate Presentation class to load the source presentation file
    with slides.Presentation(global_opts.data_dir + "welcome-to-powerpoint.pptx") as pres:
        # Get the slide whose position is to be changed
        slide = pres.slides[0]

        # Set the new position for the slide
        slide.slide_number = 2

        # Write the presentation to disk
        pres.save(global_opts.out_dir + "crud_change_position_out.pptx", slides.export.SaveFormat.PPTX)
