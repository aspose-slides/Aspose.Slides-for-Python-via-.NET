import aspose.slides as slides


#ExStart:SetTransitionEffects
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Create an instance of Presentation class
with slides.Presentation(dataDir + "welcome-to-powerpoint.pptx") as presentation:

    # Set effect
    presentation.slides[0].slide_show_transition.type = slides.slideshow.TransitionType.CUT
    presentation.slides[0].slide_show_transition.value.from_black = True

    # Write the presentation to disk
    presentation.save(outDir + "transition_SetTransitionEffects_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:SetTransitionEffects