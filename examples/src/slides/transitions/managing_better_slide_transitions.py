import aspose.slides as slides


def managing_better_slide_transitions(global_opts):
    # Instantiate Presentation class to load the source presentation file
    with slides.Presentation(global_opts.data_dir + "welcome-to-powerpoint.pptx") as presentation:
        # Apply circle type transition on slide 1
        presentation.slides[0].slide_show_transition.type = slides.slideshow.TransitionType.CIRCLE

        # Set the transition time of 3 seconds
        presentation.slides[0].slide_show_transition.advance_on_click = True
        presentation.slides[0].slide_show_transition.advance_after_time = 3000

        # Apply comb type transition on slide 2
        presentation.slides[1].slide_show_transition.type = slides.slideshow.TransitionType.COMB

        # Set the transition time of 5 seconds
        presentation.slides[1].slide_show_transition.advance_on_click = True
        presentation.slides[1].slide_show_transition.advance_after_time = 5000

        # Write the presentation to disk
        presentation.save(global_opts.out_dir + "transition_BetterTransitions_out.pptx", slides.export.SaveFormat.PPTX)
