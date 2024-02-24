import aspose.slides as slides


def get_effective_values(global_opts):
    with slides.Presentation(global_opts.data_dir + "text_add_animation_effect.pptx") as pres:
        shape = pres.slides[0].shapes[0]

        local_text_frame_format = shape.text_frame.text_frame_format
        effective_text_frame_format = local_text_frame_format.get_effective()

        local_portion_format = shape.text_frame.paragraphs[0].portions[0].portion_format
        effective_portion_format = local_portion_format.get_effective()
