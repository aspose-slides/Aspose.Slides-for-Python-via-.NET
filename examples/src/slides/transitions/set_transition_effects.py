import aspose.slides as slides


def set_transition_effects(global_opts):
    # Create an instance of Presentation class
    with slides.Presentation(global_opts.data_dir + "welcome-to-powerpoint.pptx") as presentation:
        # Set effect
        presentation.slides[0].slide_show_transition.type = slides.slideshow.TransitionType.CUT
        presentation.slides[0].slide_show_transition.value.from_black = True

        # Write the presentation to disk
        presentation.save(global_opts.out_dir + "transition_SetTransitionEffects_out.pptx", slides.export.SaveFormat.PPTX)
