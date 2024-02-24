import aspose.slides as slides


def animation_effect_in_paragraph(global_opts):
    with slides.Presentation(global_opts.data_dir + "text_add_animation_effect.pptx") as presentation:
        # select paragraph to add effect
        auto_shape = presentation.slides[0].shapes[0]
        paragraph = auto_shape.text_frame.paragraphs[0]

        # add Fly animation effect to selected paragraph
        effect = presentation.slides[0].timeline.main_sequence.add_effect(paragraph, slides.animation.EffectType.FLY,
                                                                          slides.animation.EffectSubtype.LEFT,
                                                                          slides.animation.EffectTriggerType.ON_CLICK)

        presentation.save(global_opts.out_dir + "text_add_animation_effect_out.pptx", slides.export.SaveFormat.PPTX)
