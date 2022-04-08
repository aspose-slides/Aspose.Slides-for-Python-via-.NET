import aspose.slides as slides


#ExStart:SetSizeAndType
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Instantiate a Presentation object that represents a presentation file 
with slides.Presentation(dataDir + "welcome-to-powerpoint.pptx") as presentation:
    with slides.Presentation() as auxPresentation:

        slide = presentation.slides[0]

        # Set the slide size of generated presentations to that of source
        auxPresentation.slide_size.set_size(presentation.slide_size.type,slides.SlideSizeScaleType.ENSURE_FIT)

        auxPresentation.slides.insert_clone(0, slide)
        auxPresentation.slides.remove_at(0)
        # Save Presentation to disk
        auxPresentation.save(outDir + "layout_slide_size_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:SetSizeAndType