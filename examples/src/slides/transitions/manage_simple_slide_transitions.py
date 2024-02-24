import aspose.slides as slides


def manage_simple_slide_transitions(global_opts):
    # Instantiate Presentation class to load the source presentation file
    with slides.Presentation(global_opts.data_dir + "welcome-to-powerpoint.pptx") as presentation:
        # Apply circle type transition on slide 1
        presentation.slides[0].slide_show_transition.type = slides.slideshow.TransitionType.CIRCLE

        # Apply comb type transition on slide 2
        presentation.slides[1].slide_show_transition.type = slides.slideshow.TransitionType.COMB

        # Write the presentation to disk
        presentation.save(global_opts.out_dir + "transition_add_transition_out.pptx", slides.export.SaveFormat.PPTX)
