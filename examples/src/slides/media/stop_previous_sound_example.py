import aspose.slides as slides


def stop_previous_sound_example(global_opts):
    with slides.Presentation(global_opts.data_dir + "AnimationStopSound.pptx") as pres:
        # Gets the first effect of the first slide.
        first_slide_effect = pres.slides[0].timeline.main_sequence[0]

        # Gets the first effect of the second slide.
        second_slide_effect = pres.slides[1].timeline.main_sequence[0]

        if first_slide_effect.sound is not None:
            # Changes the second effect Enhancements/Sound to "Stop Previous Sound"
            second_slide_effect.stop_previous_sound = True
            
        pres.save(global_opts.out_dir + "AnimationStopSound-out.pptx", slides.export.SaveFormat.PPTX)
