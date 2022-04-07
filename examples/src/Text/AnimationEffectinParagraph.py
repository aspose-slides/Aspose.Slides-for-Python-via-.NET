import aspose.slides as slides


# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

#ExStart:AnimationEffectinParagraph
with slides.Presentation(dataDir + "text_add_animation_effect.pptx") as presentation:
    # select paragraph to add effect
    autoShape = presentation.slides[0].shapes[0]
    paragraph = autoShape.text_frame.paragraphs[0]

    # add Fly animation effect to selected paragraph
    effect = presentation.slides[0].timeline.main_sequence.add_effect(paragraph, slides.animation.EffectType.FLY, slides.animation.EffectSubtype.LEFT, slides.animation.EffectTriggerType.ON_CLICK)


    presentation.save(outDir + "text_add_animation_effect_out.pptx", slides.export.SaveFormat.PPTX)

#ExEnd:AnimationEffectinParagraph