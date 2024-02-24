import aspose.slides as slides


def change_smart_art_shape_style(global_opts):
    with slides.Presentation(global_opts.data_dir + "smart_art_access.pptx") as presentation:
        # Traverse through every shape inside first slide
        for shape in presentation.slides[0].shapes:
            # Check if shape is of SmartArt type
            if type(shape) is slides.smartart.SmartArt:
                # Typecast shape to SmartArt
                # Checking SmartArt style
                if shape.quick_style == slides.smartart.SmartArtQuickStyleType.SIMPLE_FILL:
                    # Changing SmartArt Style
                    shape.quick_style = slides.smartart.SmartArtQuickStyleType.CARTOON

        # Saving Presentation
        presentation.save(global_opts.out_dir + "smart_art_change_quick_style_out.pptx", slides.export.SaveFormat.PPTX)
