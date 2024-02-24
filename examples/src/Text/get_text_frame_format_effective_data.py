import aspose.slides as slides


def get_text_frame_format_effective_data(global_opts):
    with slides.Presentation(global_opts.data_dir + "text_add_animation_effect.pptx") as pres:
        shape = pres.slides[0].shapes[0]

        text_frame_format = shape.text_frame.text_frame_format
        effective_text_frame_format = text_frame_format.get_effective()

        print("Anchoring type: " + str(effective_text_frame_format.anchoring_type))
        print("Autofit type: " + str(effective_text_frame_format.autofit_type))
        print("Text vertical type: " + str(effective_text_frame_format.text_vertical_type))
        print("Margins")
        print("   Left: " + str(effective_text_frame_format.margin_left))
        print("   Top: " + str(effective_text_frame_format.margin_top))
        print("   Right: " + str(effective_text_frame_format.margin_right))
        print("   Bottom: " + str(effective_text_frame_format.margin_bottom))
