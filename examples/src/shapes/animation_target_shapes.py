import aspose.slides as slides


def animation_target_shapes(global_opts):
    with slides.Presentation(global_opts.data_dir + "shapes_animation_example.pptx") as pres:
        for slide in pres.slides:
            for effect in slide.timeline.main_sequence:
                print("{0} animation effect is set to shape#{1} on slide#{2}".format(effect.type,
                                                                                     effect.target_shape.unique_id,
                                                                                     slide.slide_number))
