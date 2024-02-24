import aspose.slides as slides


def get_text_style_effective_data(global_opts):
    with slides.Presentation(global_opts.data_dir + "text_add_animation_effect.pptx") as pres:
        shape = pres.slides[0].shapes[0]
        effective_text_style = shape.text_frame.text_frame_format.text_style.get_effective()

        for i in range(9):
            effective_style_level = effective_text_style.get_level(i)
            print("= Effective paragraph formatting for style level #" + str(i) + " =")

            print("depth: " + str(effective_style_level.depth))
            print("Indent: " + str(effective_style_level.indent))
            print("Alignment: " + str(effective_style_level.alignment))
            print("Font alignment: " + str(effective_style_level.font_alignment))
