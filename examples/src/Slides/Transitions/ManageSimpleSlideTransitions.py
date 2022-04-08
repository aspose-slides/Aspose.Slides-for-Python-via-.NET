import aspose.slides as slides


#ExStart:ManageSimpleSlideTransitions
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Instantiate Presentation class to load the source presentation file
with slides.Presentation(dataDir + "welcome-to-powerpoint.pptx") as presentation:
    # Apply circle type transition on slide 1
    presentation.slides[0].slide_show_transition.type = slides.slideshow.TransitionType.CIRCLE

    # Apply comb type transition on slide 2
    presentation.slides[1].slide_show_transition.type = slides.slideshow.TransitionType.COMB

    # Write the presentation to disk
    presentation.save(outDir + "transition_add_transition_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:ManageSimpleSlideTransitions