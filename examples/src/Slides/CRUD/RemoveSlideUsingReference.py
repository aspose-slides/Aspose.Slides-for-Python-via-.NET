import aspose.slides as slides


#ExStart:RemoveSlideUsingReference
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Instantiate a Presentation object that represents a presentation file
with slides.Presentation(dataDir + "welcome-to-powerpoint.pptx") as pres:
    # Accessing a slide using its index in the slides collection
    slide = pres.slides[0]

    # Removing a slide using its reference
    pres.slides.remove(slide)

    #Writing the presentation file
    pres.save(outDir + "crud_remove_slide_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:RemoveSlideUsingReference