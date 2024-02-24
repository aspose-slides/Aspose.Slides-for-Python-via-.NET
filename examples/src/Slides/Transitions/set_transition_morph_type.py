import aspose.slides as slides


def set_transition_morph_type(global_opts):
    with slides.Presentation(global_opts.data_dir + "welcome-to-powerpoint.pptx") as presentation:
        presentation.slides[0].slide_show_transition.type = slides.slideshow.TransitionType.MORPH
        presentation.slides[0].slide_show_transition.value.morph_type = slides.slideshow.TransitionMorphType.BY_WORD
        presentation.save(global_opts.out_dir + "transition_MORPH_out.pptx", slides.export.SaveFormat.PPTX)
