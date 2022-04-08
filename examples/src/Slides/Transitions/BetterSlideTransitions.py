import aspose.slides as slides


#ExStart:BetterSlideTransitions
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Instantiate Presentation class that represents a presentation file
with slides.Presentation(dataDir + "transitions.pptx") as pres:
    # Apply circle type transition on slide 1
    pres.slides[0].slide_show_transition.type = slides.slideshow.TransitionType.CIRCLE


    # Set the transition time of 3 seconds
    pres.slides[0].slide_show_transition.advance_on_click = True
    pres.slides[0].slide_show_transition.advance_after_time = 3000

    # Apply comb type transition on slide 2
    pres.slides[1].slide_show_transition.type = slides.slideshow.TransitionType.COMB


    # Set the transition time of 5 seconds
    pres.slides[1].slide_show_transition.advance_on_click = True
    pres.slides[1].slide_show_transition.advance_after_time = 5000

    # Apply zoom type transition on slide 3
    pres.slides[2].slide_show_transition.type = slides.slideshow.TransitionType.ZOOM


    # Set the transition time of 7 seconds
    pres.slides[2].slide_show_transition.advance_on_click = True
    pres.slides[2].slide_show_transition.advance_after_time = 7000

    # Write the presentation to disk
    pres.save(outDir + "transition_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:BetterSlideTransitions