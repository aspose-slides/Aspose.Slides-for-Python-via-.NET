import aspose.slides as slides


def animation_rewind(global_opts):
    # Instantiate Presentation class that represents a presentation file
    with slides.Presentation(global_opts.data_dir + "AnimationRewind.pptx") as presentation:
        # Gets the effects sequence for the first slide
        effects_sequence = presentation.slides[0].timeline.main_sequence
        
        # Gets the first effect of the main sequence.
        effect = effects_sequence[0]
        print("\nEffect Timing/Rewind in source presentation is {0}".format(effect.timing.rewind))
        # Turns the effect Timing/Rewind on.
        effect.timing.rewind = True
        
        # Save presentation
        presentation.save(global_opts.out_dir + "AnimationRewind-out.pptx", slides.export.SaveFormat.PPTX)

        with slides.Presentation(global_opts.out_dir + "AnimationRewind-out.pptx") as pres:
            # Gets the effects sequence for the first slide
            effects_sequence = pres.slides[0].timeline.main_sequence
            
            # Gets the first effect of the main sequence.
            effect = effects_sequence[0]
            print("Effect Timing/Rewind in destination presentation is {0}\n".format(effect.timing.rewind))
