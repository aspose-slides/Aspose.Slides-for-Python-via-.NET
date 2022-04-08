import aspose.slides as slides


#ExStart:SetTransitionMorphType
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

with slides.Presentation(dataDir + "welcome-to-powerpoint.pptx") as presentation:
    presentation.slides[0].slide_show_transition.type = slides.slideshow.TransitionType.MORPH
    presentation.slides[0].slide_show_transition.value.morph_type = slides.slideshow.TransitionMorphType.BY_WORD
    presentation.save(outDir + "transition_MORPH_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:SetTransitionMorphType