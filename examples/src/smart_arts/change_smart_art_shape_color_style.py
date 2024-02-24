import aspose.slides as slides


def change_smart_art_shape_color_style(global_opts):
    # Creating a presentation instance
    with slides.Presentation(global_opts.data_dir + "smart_art_access.pptx") as presentation:
        # Traverse through every shape inside first slide
        for shape in presentation.slides[0].shapes:
            # Check if shape is of SmartArt type
            if type(shape) is slides.smartart.SmartArt:
                # Typecast shape to SmartArt
                # Checking SmartArt color type
                if shape.color_style == slides.smartart.SmartArtColorType.COLORED_FILL_ACCENT1:
                    # Changing SmartArt color type
                    shape.color_style = slides.smartart.SmartArtColorType.COLORFUL_ACCENT_COLORS

        # Saving Presentation
        presentation.save(global_opts.out_dir + "smart_art_change_color_style_out.pptx", slides.export.SaveFormat.PPTX)
