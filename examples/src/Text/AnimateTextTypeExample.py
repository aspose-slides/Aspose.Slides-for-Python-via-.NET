import aspose.slides as slides

# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

def animate_text_type_example():
    with slides.Presentation() as presentation:
        oval = presentation.slides[0].shapes.add_auto_shape(slides.ShapeType.ELLIPSE, 100, 100, 300, 150)
        oval.text_frame.text = "The new animated text"
        
        # Get anomation timeline.
        timeline = presentation.slides[0].timeline
        
        # Set the effect of the first slide.
        effect = timeline.main_sequence.add_effect(oval, slides.animation.EffectType.APPEAR, slides.animation.EffectSubtype.NONE, slides.animation.EffectTriggerType.ON_CLICK)
        
        # Set the effect Animate text type to "By letter".
        effect.animate_text_type = slides.animation.AnimateTextType.BY_LETTER
        
        # Set the delay between animated text parts.
        effect.delay_between_text_parts = -1.5
        
        # Save presentation.
        presentation.save(outDir + "AnimateTextEffect_out.pptx", slides.export.SaveFormat.PPTX)
