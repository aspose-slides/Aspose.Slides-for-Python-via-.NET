import aspose.slides as slides


def shapes_accessing_alt_text(global_opts):
    # Instantiate Presentation class that represents PPTX file
    with slides.Presentation(global_opts.data_dir + "shapes_accessing_alt_text.pptx") as pres:
        # Get the first slide
        slide = pres.slides[0]

        for shape in slide.shapes:
            if type(shape) is slides.GroupShape:
                # Accessing the group shape.

                for shape2 in shape.shapes:
                    # Accessing the AltText property
                    print(shape2.alternative_text)
