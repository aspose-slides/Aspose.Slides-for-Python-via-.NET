import aspose.slides as slides


def better_slide_transitions(global_opts):
    # Instantiate Presentation class that represents a presentation file
    with slides.Presentation(global_opts.data_dir + "transitions.pptx") as pres:
        # Apply circle type transition on slide 1
        pres.slides[0].slide_show_transition.type = slides.slideshow.TransitionType.CIRCLE

        # Set the transition time of 3 seconds
        pres.slides[0].slide_show_transition.advance_on_click = True
        pres.slides[0].slide_show_transition.advance_after_time = 3000

        # Apply comb type transition on slide 2
        pres.slides[1].slide_show_transition.type = slides.slideshow.TransitionType.COMB

        # Set the transition time of 5 seconds
        pres.slides[1].slide_show_transition.advance_on_click = True
        pres.slides[1].slide_show_transition.advance_after_time = 5000

        # Apply zoom type transition on slide 3
        pres.slides[2].slide_show_transition.type = slides.slideshow.TransitionType.ZOOM

        # Set the transition time of 7 seconds
        pres.slides[2].slide_show_transition.advance_on_click = True
        pres.slides[2].slide_show_transition.advance_after_time = 7000

        # Write the presentation to disk
        pres.save(global_opts.out_dir + "transition_out.pptx", slides.export.SaveFormat.PPTX)
