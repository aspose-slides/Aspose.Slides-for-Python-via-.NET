import aspose.slides as slides


def get_background_effective_values(global_opts):
    # Instantiate the Presentation class that represents the presentation file
    with slides.Presentation(global_opts.data_dir + "background.pptx") as pres:
        effective_background = pres.slides[0].background.get_effective()
        if effective_background.fill_format.fill_type == slides.FillType.SOLID:
            print("Fill color: " + str(effective_background.fill_format.solid_fill_color))
        else:
            print("Fill type: " + str(effective_background.fill_format.fill_type))
