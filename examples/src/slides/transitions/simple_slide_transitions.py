import aspose.slides as slides


def simple_slide_transitions(global_opts):
    # Instantiate Presentation class that represents a presentation file
    with slides.Presentation(global_opts.data_dir + "welcome-to-powerpoint.pptx") as pres:
        # Apply circle type transition on slide 1
        pres.slides[0].slide_show_transition.type = slides.slideshow.TransitionType.CIRCLE

        # Apply comb type transition on slide 2
        pres.slides[1].slide_show_transition.type = slides.slideshow.TransitionType.COMB

        # Write the presentation to disk
        pres.save(global_opts.out_dir + "transition_SampleTransition_out.pptx", slides.export.SaveFormat.PPTX)
