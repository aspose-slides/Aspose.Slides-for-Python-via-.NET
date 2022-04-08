import aspose.slides as slides


#ExStart:SimpleSlideTransitions
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Instantiate Presentation class that represents a presentation file
with slides.Presentation(dataDir + "welcome-to-powerpoint.pptx") as pres:
    # Apply circle type transition on slide 1
    pres.slides[0].slide_show_transition.type = slides.slideshow.TransitionType.CIRCLE

    # Apply comb type transition on slide 2
    pres.slides[1].slide_show_transition.type = slides.slideshow.TransitionType.COMB

    # Write the presentation to disk
    pres.save(outDir + "transition_SampleTransition_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:SimpleSlideTransitions