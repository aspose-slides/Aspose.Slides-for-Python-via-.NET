import aspose.slides as slides

# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

def stop_previous_sound():
    pptx_file = dataDir + "AnimationStopSound.pptx"
    out_path = outDir + "AnimationStopSound-out.pptx"

    with slides.Presentation(pptx_file) as pres:
        # Gets the first effect of the first slide.
        first_slide_effect = pres.slides[0].timeline.main_sequence[0]

        # Gets the first effect of the second slide.
        second_slide_effect = pres.slides[1].timeline.main_sequence[0]

        if first_slide_effect.sound is not None:
            # Changes the second effect Enhancements/Sound to "Stop Previous Sound"
            second_slide_effect.stop_previous_sound = True
            
        pres.save(out_path, slides.export.SaveFormat.PPTX)
