import aspose.slides as slides

# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

def animation_rewind():
    # Instantiate Presentation class that represents a presentation file
    with slides.Presentation(dataDir + "AnimationRewind.pptx") as presentation:
        # Gets the effects sequence for the first slide
        effects_sequence = presentation.slides[0].timeline.main_sequence
        
        # Gets the first effect of the main sequence.
        effect = effects_sequence[0]
        print("\nEffect Timing/Rewind in source presentation is {0}", effect.timing.rewind)
        # Turns the effect Timing/Rewind on.
        effect.timing.rewind = True
        
        # Save presentation
        presentation.save(outDir + "AnimationRewind-out.pptx", slides.export.SaveFormat.PPTX)
        
        
        with slides.Presentation(outDir + "AnimationRewind-out.pptx") as pres:
            # Gets the effects sequence for the first slide
            effects_sequence = pres.slides[0].timeline.main_sequence
            
            # Gets the first effect of the main sequence.
            effect = effects_sequence[0]
            print("Effect Timing/Rewind in destination presentation is {0}\n", effect.timing.rewind)
